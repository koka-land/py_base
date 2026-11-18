const delay = ms => new Promise(res => setTimeout(res, ms));

const SKILL_LEVELS = {
    2: "Редко",
    3: "Часто",
    4: "Почти всегда"
};

function getVariedSkills(average, gradesCount, hwRatio, numQuestions) {
    let levels = [];
    for (let i = 0; i < numQuestions; i++) {
        let base = average >= 4.5 ? 4 : (average >= 3.5 ? 3 : 2);

        if (i === 0 || i === 1) {
            if (hwRatio >= 0.8) base = (average >= 3.5) ? 4 : 3;
            else if (hwRatio <= 0.4) base = Math.min(base, 2);
        } else {
            if (gradesCount >= 5 && hwRatio > 0.7) {
                if (Math.random() < 0.3 && base < 4) base += 1;
            } else if (gradesCount <= 2 || hwRatio < 0.4) {
                if (Math.random() < 0.3 && base > 2) base -= 1;
            }
            if (Math.random() < 0.1) {
                if (base === 4) base = 3;
                else if (base === 3) base = Math.random() < 0.5 ? 2 : 4;
            }
        }
        levels.push(base);
    }
    return levels;
}

function getElementByExactText(tag, text) {
    return Array.from(document.querySelectorAll(tag)).find(el => el.textContent.trim() === text);
}

function closeStudentModal() {
    let titleEl = getElementByExactText('div', 'Информация об учащемся');
    if (titleEl && titleEl.parentElement) {
        let closeBtn = titleEl.parentElement.querySelector('button');
        if (closeBtn) {
            closeBtn.click();
            return;
        }
    }
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
}

async function switchToFirstClass() {
    let dropdownWrapper = document.querySelector('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]');
    if (!dropdownWrapper) return false;

    dropdownWrapper.click();
    await delay(1200);

    let options = Array.from(document.querySelectorAll('li, [role="option"]')).filter(el => {
        let rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0 && !el.closest('nav') && !el.closest('header');
    });

    if (options.length === 0) {
        document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
        return false;
    }

    options[0].click();
    await delay(3500);
    return true;
}

async function switchNextClass(currentClassName) {
    let dropdownWrapper = document.querySelector('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]');
    if (!dropdownWrapper) return false;

    dropdownWrapper.click();
    await delay(1200);

    let options = Array.from(document.querySelectorAll('li, [role="option"]')).filter(el => {
        let rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0 && !el.closest('nav') && !el.closest('header');
    });

    if (options.length === 0) {
        document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
        return false;
    }

    let currentIndex = options.findIndex(item => item.textContent.trim().includes(currentClassName));

    if (currentIndex !== -1 && currentIndex + 1 < options.length) {
        options[currentIndex + 1].click();
        await delay(3500);
        return true;
    }

    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
    return false;
}

async function processClass(forceRecalc) {
    let studentSpans = document.querySelectorAll("tbody span[title]");
    if (studentSpans.length === 0) return { processed: 0, alreadySet: 0, aborted: false };

    let hwLessonIds = [];
    let cdzHeaders = Array.from(document.querySelectorAll('th')).filter(th => th.textContent.includes("ЦДЗ"));

    cdzHeaders.forEach(header => {
        let div = header.querySelector('div[data-test-component]');
        if (div) {
            let attr = div.getAttribute("data-test-component");
            let parts = attr.split("_");
            if (parts.length >= 2) {
                let match = parts[0].match(/\d+/);
                if (match) hwLessonIds.push(match[0]);
            }
        }
    });

    let alreadySetCount = 0;
    let processedCount = 0;

    for (let i = 0; i < studentSpans.length; i++) {
        // Проверка на экстренную остановку
        if (window.meshRobotStopRequested) {
            return { processed: processedCount, alreadySet: alreadySetCount, aborted: true };
        }

        let span = studentSpans[i];
        let row = span.closest('tr');
        if (!row) continue;

        let cells = row.querySelectorAll('td');
        let gradeText = cells[cells.length - 1].textContent.trim().replace(',', '.');
        if (!gradeText || gradeText === "-") continue;

        let grade = parseFloat(gradeText);
        let gradesCount = 0;
        let hwCompleted = 0;

        let markDivs = row.querySelectorAll('div[data-test-component^="markCell-"]');
        markDivs.forEach(div => {
            let text = div.textContent.trim();
            let hasGrade = ['5','4','3','2','1'].includes(text);
            if (hasGrade) gradesCount++;

            let attr = div.getAttribute("data-test-component");
            if (attr) {
                let parts = attr.split("_");
                if (parts.length >= 3 && hwLessonIds.includes(parts[1])) {
                    if (hasGrade || (text !== "" && !['н','нб','нв'].includes(text.toLowerCase()))) {
                        hwCompleted++;
                    }
                }
            }
        });

        let hwRatio = hwLessonIds.length > 0 ? hwCompleted / hwLessonIds.length : 1.0;

        span.click();
        await delay(800);

        // Вторая проверка после паузы (вдруг нажали Стоп, пока открывалось окно)
        if (window.meshRobotStopRequested) {
            closeStudentModal();
            return { processed: processedCount, alreadySet: alreadySetCount, aborted: true };
        }

        let revalBtn = getElementByExactText('button', 'Повторно оценить учебные умения');
        let evalBtn = getElementByExactText('button', 'Оценить учебные умения');

        if (revalBtn) {
            if (forceRecalc) {
                revalBtn.click();
            } else {
                alreadySetCount++;
                closeStudentModal();
                await delay(400);
                continue;
            }
        } else if (evalBtn) {
            evalBtn.click();
        } else {
            closeStudentModal();
            await delay(400);
            continue;
        }

        await delay(1500);

        if (window.meshRobotStopRequested) {
            closeStudentModal();
            return { processed: processedCount, alreadySet: alreadySetCount, aborted: true };
        }

        let options2 = Array.from(document.querySelectorAll('label')).filter(l => l.textContent.includes('Редко'));
        let numQuestions = options2.length;

        if (numQuestions === 0) {
            document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
            await delay(400);
            continue;
        }

        let levels = getVariedSkills(grade, gradesCount, hwRatio, numQuestions);

        for (let q = 0; q < numQuestions; q++) {
            if (q === 0) {
                let dummys = Array.from(document.querySelectorAll('label')).filter(l => l.textContent.includes('Почти никогда'));
                if (dummys.length > 0) {
                    dummys[0].click();
                    await delay(150);
                }
            }

            let targetText = SKILL_LEVELS[levels[q]];
            let targets = Array.from(document.querySelectorAll('label')).filter(l => l.textContent.includes(targetText));

            if (targets[q]) {
                targets[q].click();
                await delay(250);
            }
        }

        await delay(500);
        let saveBtn = getElementByExactText('button', 'Сохранить');
        if (saveBtn) saveBtn.click();

        await delay(2000);

        // Подстраховка: если мы нажали сохранить, окно закрывается само,
        // но если произошел стоп в этот момент, попытаемся закрыть окно крестиком
        if (window.meshRobotStopRequested) {
            closeStudentModal();
            processedCount++;
            return { processed: processedCount, alreadySet: alreadySetCount, aborted: true };
        }

        let closeBtn = getElementByExactText('button', 'Закрыть');
        if (closeBtn) closeBtn.click();

        processedCount++;
        await delay(800);
    }

    return { processed: processedCount, alreadySet: alreadySetCount, aborted: false };
}

async function runRobot(forceRecalc, processAll) {
    if (window.isMeshRobotRunning) {
        alert("Робот уже работает! Вы можете остановить его кнопкой в меню.");
        return;
    }

    window.isMeshRobotRunning = true;
    window.meshRobotStopRequested = false;

    let globalStats = { processed: 0, alreadySet: 0, classes: 0 };

    if (processAll) {
        let switchedToFirst = await switchToFirstClass();
        if (!switchedToFirst || window.meshRobotStopRequested) {
            if (!window.meshRobotStopRequested) alert("Не удалось открыть список классов.");
            window.isMeshRobotRunning = false;
            return;
        }
    }

    do {
        if (window.meshRobotStopRequested) break;

        let dropdownWrapper = document.querySelector('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]');
        let currentClass = dropdownWrapper ? dropdownWrapper.textContent.trim() : "Текущий класс";

        let stats = await processClass(forceRecalc);
        globalStats.processed += stats.processed;
        globalStats.alreadySet += stats.alreadySet;
        globalStats.classes++;

        if (stats.aborted || window.meshRobotStopRequested || !processAll) break;

        let hasNext = await switchNextClass(currentClass);
        if (!hasNext) break;

    } while (true);

    if (window.meshRobotStopRequested) {
        alert(`🚨 ЭКСТРЕННАЯ ОСТАНОВКА!\n\nУспели пройти классов: ${globalStats.classes}\nВыставлено: ${globalStats.processed}\nПропущено: ${globalStats.alreadySet}`);
    } else {
        alert(`ОБХОД ЗАВЕРШЕН!\n\nКлассов пройдено: ${globalStats.classes}\nУспешно выставлено: ${globalStats.processed}\nУже стояли (пропущено): ${globalStats.alreadySet}`);
    }

    window.isMeshRobotRunning = false;
    window.meshRobotStopRequested = false;
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "start") {
        runRobot(request.forceRecalc, request.processAll);
    } else if (request.action === "stop") {
        window.meshRobotStopRequested = true;
    }
});