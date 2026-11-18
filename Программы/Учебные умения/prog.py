import re
import random
from playwright.sync_api import sync_playwright

SKILL_LEVELS = {
    2: "Редко",
    3: "Часто",
    4: "Почти всегда"
}

DUMMY_TEXT = "Почти никогда"


def get_skill_text(average_grade):
    grade = float(average_grade)
    if grade >= 4.5:
        return SKILL_LEVELS[4]
    elif grade >= 3.5:
        return SKILL_LEVELS[3]
    else:
        return SKILL_LEVELS[2]


def get_varied_skills(average, grades_count, hw_ratio, num_questions):
    levels = []
    for i in range(num_questions):
        if average >= 4.5:
            base = 4
        elif average >= 3.5:
            base = 3
        else:
            base = 2

        if i in [0, 1]:
            if hw_ratio >= 0.8:
                base = 4 if average >= 3.5 else 3
            elif hw_ratio <= 0.4:
                base = min(base, 2)
        else:
            if grades_count >= 5 and hw_ratio > 0.7:
                if random.random() < 0.3 and base < 4:
                    base += 1
            elif grades_count <= 2 or hw_ratio < 0.4:
                if random.random() < 0.3 and base > 2:
                    base -= 1

            if random.random() < 0.1:
                if base == 4:
                    base = 3
                elif base == 3:
                    base = random.choice([2, 4])

        levels.append(base)
    return levels


def close_student_modal(page):
    try:
        header_div = page.locator('text="Информация об учащемся"').locator('xpath=..').first
        header_div.locator('button').first.click(timeout=1000)
    except:
        page.mouse.click(10, 10)
        page.keyboard.press("Escape")
    page.wait_for_timeout(400)


def process_single_class(page, class_name, force_recalc=False):
    student_names = page.locator("tbody span[title]").all()
    real_students_count = len(student_names)

    already_set_count = 0
    processed_count = 0
    no_grade_count = 0
    error_names = []

    print(f"\n--- Сканирую учеников: {class_name} ---")

    hw_lesson_ids = []
    cdz_headers = page.locator('th').filter(has_text="ЦДЗ").all()

    for header in cdz_headers:
        attr = header.locator('div[data-test-component]').first.get_attribute("data-test-component")
        if attr:
            parts = attr.split("_")
            if len(parts) >= 2:
                lesson_id_match = re.search(r'\d+', parts[0])
                if lesson_id_match:
                    hw_lesson_ids.append(lesson_id_match.group())

    if hw_lesson_ids:
        print(f"Распознано колонок с ДЗ (ЦДЗ): {len(hw_lesson_ids)}")
    else:
        print("В этом классе колонок с ДЗ не обнаружено.")

    for student_span in student_names:
        name = "Неизвестно"
        try:
            name = student_span.get_attribute("title")
            if not name:
                continue

            row = student_span.locator("xpath=ancestor::tr").first

            last_cell = row.locator("td").last
            grade_text = last_cell.inner_text().strip().replace(',', '.')
            if not grade_text or grade_text == "-" or grade_text == "":
                no_grade_count += 1
                continue
            grade = float(grade_text)

            grades_count = 0
            hw_completed = 0

            mark_cells = row.locator('div[data-test-component^="markCell-"]').all()
            for cell in mark_cells:
                text = cell.inner_text().strip()
                has_grade = text in ['5', '4', '3', '2', '1']

                if has_grade:
                    grades_count += 1

                attr = cell.get_attribute("data-test-component")
                if attr:
                    parts = attr.split("_")
                    if len(parts) >= 3:
                        lesson_id = parts[1]
                        if lesson_id in hw_lesson_ids:
                            if has_grade or (text != "" and text.lower() not in ['н', 'нб', 'нв']):
                                hw_completed += 1

            hw_total = len(hw_lesson_ids)
            hw_ratio = hw_completed / hw_total if hw_total > 0 else 1.0

            student_span.click()
            page.wait_for_timeout(800)

            reval_button = page.get_by_text("Повторно оценить учебные умения", exact=True).first
            eval_button = page.get_by_text("Оценить учебные умения", exact=True).first

            if reval_button.is_visible():
                if force_recalc:
                    reval_button.click()
                else:
                    already_set_count += 1
                    close_student_modal(page)
                    continue
            elif eval_button.is_visible():
                eval_button.click()
            else:
                error_names.append(name)
                close_student_modal(page)
                continue

            page.locator("text='Самоорганизация'").wait_for(state="visible", timeout=3000)
            page.wait_for_timeout(1500)

            options_1 = page.get_by_text("Почти никогда", exact=True).all()
            options_2 = page.get_by_text("Редко", exact=True).all()
            options_3 = page.get_by_text("Часто", exact=True).all()
            options_4 = page.get_by_text("Почти всегда", exact=True).all()

            num_questions = len(options_2)
            if num_questions == 0:
                error_names.append(name)
                page.keyboard.press("Escape")
                continue

            levels = get_varied_skills(grade, grades_count, hw_ratio, num_questions)
            print(f"[{name}] Ср.балл: {grade}, Оценок: {grades_count}, Сдано ДЗ: {int(hw_ratio * 100)}%")

            for i in range(num_questions):
                if i == 0 and len(options_1) > 0:
                    options_1[0].click()
                    page.wait_for_timeout(150)

                target = levels[i]
                if target == 4 and i < len(options_4):
                    options_4[i].click()
                elif target == 3 and i < len(options_3):
                    options_3[i].click()
                elif target == 2 and i < len(options_2):
                    options_2[i].click()

                page.wait_for_timeout(200)

            page.wait_for_timeout(500)
            save_button = page.get_by_text("Сохранить", exact=True)
            save_button.click()

            close_button = page.get_by_text("Закрыть", exact=True)
            close_button.wait_for(state="visible", timeout=5000)
            page.wait_for_timeout(500)
            close_button.click()

            processed_count += 1
            page.wait_for_timeout(800)

        except Exception as e:
            if name not in error_names and name != "Неизвестно":
                error_names.append(name)
            page.mouse.click(10, 10)
            page.keyboard.press("Escape")
            page.wait_for_timeout(800)
            continue

    return {
        "name": class_name,
        "total": real_students_count,
        "already_set": already_set_count,
        "processed": processed_count,
        "no_grade": no_grade_count,
        "error_names": error_names
    }


def run_agent():
    print("\n" + "=" * 50)
    print(" РОБОТ-ПЕДАГОГ ДЛЯ МЭШ (ВЫСТАВЛЕНИЕ УМЕНИЙ)")
    print("=" * 50)

    ans = input("\nПереоценивать детей, у которых навыки уже выставлены? (д/н) [по умолчанию - н]: ").strip().lower()
    force_recalc = ans in ['д', 'да', 'y', 'yes']

    with sync_playwright() as p:
        print("\nПодключаюсь к открытому Chrome (порт 9222)...")
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return

        default_context = browser.contexts[0]
        page = None
        for p_tab in default_context.pages:
            if "school.mos.ru" in p_tab.url:
                page = p_tab
                break

        if not page:
            print("ОШИБКА: Не найдена вкладка school.mos.ru!")
            return

        page.bring_to_front()
        dropdown = page.locator('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]')

        all_stats = []
        prev_class_name = ""
        class_index = 1

        while True:
            tabs_to_press = class_index + 1

            print(f"\nОткрываю список, нажимаю Tab {tabs_to_press} раз(а)...")
            if dropdown.is_visible():
                dropdown.click()
                page.wait_for_timeout(1000)

                for _ in range(tabs_to_press):
                    page.keyboard.press("Tab")
                    page.wait_for_timeout(250)

                page.keyboard.press("Enter")
                page.wait_for_timeout(3500)

            try:
                page.wait_for_selector("tbody span[title]", state="visible", timeout=15000)
            except:
                print("Таблица не прогрузилась. Возможно, список классов закончился.")
                break

            current_class_name = dropdown.inner_text().strip()

            if current_class_name == prev_class_name:
                print("\nДостигнут конец списка классов (названия перестали меняться).")
                break

            max_attempts = 2
            for attempt in range(max_attempts):
                stats = process_single_class(page, current_class_name, force_recalc)
                if not stats['error_names']:
                    all_stats.append(stats)
                    break
                else:
                    if attempt < max_attempts - 1:
                        print(f"[{current_class_name}] Обнаружены ошибки у: {', '.join(stats['error_names'])}.")
                        print("Запускаю повторный анализ проблемных карточек этого же класса...")
                        page.wait_for_timeout(1500)
                    else:
                        all_stats.append(stats)

            prev_class_name = current_class_name
            class_index += 1

        print("\n" + "=" * 70)
        print("ИТОГОВАЯ СТАТИСТИКА ПО КЛАССАМ:")
        print("=" * 70)
        total_processed, total_already_set, total_errors = 0, 0, 0

        for stat in all_stats:
            status = "ГОТОВ" if not stat['error_names'] else "ТРЕБУЕТ ВНИМАНИЯ"
            print(f"\n[{status}] {stat['name']}")
            print(f"  Уже стояли: {stat['already_set']} | Успешно: {stat['processed']} | Всего детей: {stat['total']}")
            if stat['error_names']:
                print(f"  ОШИБКИ ({len(stat['error_names'])}): {', '.join(stat['error_names'])}")

            total_processed += stat['processed']
            total_already_set += stat['already_set']
            total_errors += len(stat['error_names'])

        print("\n" + "=" * 70)
        print("ОБЩИЙ ИТОГ РАБОТЫ РОБОТА-ПЕДАГОГА:")
        print(f"Всего классов пройдено: {len(all_stats)}")
        print(f"Новых умений выставлено: {total_processed}")
        print(f"Сохранено ранее (пропущено): {total_already_set}")
        print(f"Осталось нерешенных ошибок: {total_errors}")
        print("=" * 70 + "\n")

        input("Нажмите Enter, чтобы закрыть окно...")
        browser.close()


if __name__ == "__main__":
    run_agent()