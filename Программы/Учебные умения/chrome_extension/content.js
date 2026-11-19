(() => {
    const delay = ms => new Promise(res => setTimeout(res, ms));

    const DEFAULT_SETTINGS = {
        autoOpenJournalPanel: true,
        highThreshold: 4.5,
        midThreshold: 3.5,
        lowThreshold: 2.5,
        absenceRatio: 0.5
    };

    const SKILL_LABELS = {
        1: "Почти никогда",
        2: "Редко",
        3: "Часто",
        4: "Почти всегда",
        5: "Затрудняюсь ответить"
    };

    const IMPORTANT_KEYWORDS = [
        "к/р", "с/р", "контрольн", "самостоятельн",
        "тест", "проверочн", "практическ", "диктант", "сочинен"
    ];

    const STANDARD_QUESTIONS = [
        { question_group_name: "Самоорганизация", questions: [{ question_id: 1 }, { question_id: 2 }] },
        { question_group_name: "Самообразование", questions: [{ question_id: 3 }, { question_id: 4 }] },
        { question_group_name: "Саморегуляция", questions: [{ question_id: 5 }, { question_id: 6 }, { question_id: 7 }] },
        { question_group_name: "Коммуникация", questions: [{ question_id: 11 }, { question_id: 13 }, { question_id: 14 }] }
    ];

    function parseRgbColor(colorStr) {
        if (!colorStr) return null;
        const match = colorStr.match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,/\s]+([\d.]+))?\s*\)/i);
        if (!match) return null;
        const alpha = match[4] !== undefined ? parseFloat(match[4]) : 1;
        if (Number.isNaN(alpha) || alpha <= 0.05) return null;
        return {
            r: Math.min(255, Math.max(0, Math.round(parseFloat(match[1])))),
            g: Math.min(255, Math.max(0, Math.round(parseFloat(match[2])))),
            b: Math.min(255, Math.max(0, Math.round(parseFloat(match[3]))))
        };
    }

    function rgbToCss({ r, g, b }) {
        return `rgb(${r}, ${g}, ${b})`;
    }

    function rgbToRgba({ r, g, b }, alpha) {
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }

    function getLuminance({ r, g, b }) {
        const toLinear = v => {
            const s = v / 255;
            return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
        };
        return 0.2126 * toLinear(r) + 0.7152 * toLinear(g) + 0.0722 * toLinear(b);
    }

    function getSaturation({ r, g, b }) {
        const max = Math.max(r, g, b) / 255;
        const min = Math.min(r, g, b) / 255;
        if (max === min) return 0;
        const l = (max + min) / 2;
        const d = max - min;
        return l > 0.5 ? d / (2 - max - min) : d / (max + min);
    }

    function extractJournalTheme() {
        try {
            const leftMenu =
                document.querySelector("aside, nav, [class*='sidebar' i], [class*='Sidebar' i], [class*='leftMenu' i], [class*='left-menu' i]") ||
                null;

            if (!leftMenu) {
                return null;
            }

            const menuStyle = window.getComputedStyle(leftMenu);
            const menuBgRgb = parseRgbColor(menuStyle.backgroundColor);

            // Если у самого <aside>/<nav> фон прозрачный, ищем фон внутри контейнера меню
            let effectiveMenuBg = menuBgRgb;
            if (!effectiveMenuBg) {
                const menuChildren = Array.from(leftMenu.querySelectorAll("div, ul, section"));
                for (const child of menuChildren) {
                    const st = window.getComputedStyle(child);
                    const c = parseRgbColor(st.backgroundColor);
                    const rect = child.getBoundingClientRect();
                    if (c && rect.width > 120 && rect.height > 200) {
                        effectiveMenuBg = c;
                        break;
                    }
                }
            }

            if (!effectiveMenuBg) {
                return null;
            }

            const isMenuDark = getLuminance(effectiveMenuBg) < 0.35;

            // Ищем акцентный цвет активного пункта левого меню (например, «Журналы классов»)
            let activeAccentRgb = null;
            const activeSelectors = [
                "[aria-current='page']",
                "[aria-selected='true']",
                ".active",
                "[class*='active' i]",
                "[class*='selected' i]",
                "[class*='current' i]"
            ];

            for (const sel of activeSelectors) {
                const candidates = Array.from(leftMenu.querySelectorAll(sel));
                for (const item of candidates) {
                    const rect = item.getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) continue;
                    const st = window.getComputedStyle(item);
                    const bgCandidate = parseRgbColor(st.backgroundColor);
                    if (bgCandidate && getSaturation(bgCandidate) > 0.25) {
                        const lum = getLuminance(bgCandidate);
                        if (lum > 0.03 && lum < 0.85) {
                            activeAccentRgb = bgCandidate;
                            break;
                        }
                    }
                }
                if (activeAccentRgb) break;
            }

            // Запасной поиск насыщенного цвета внутри левого меню
            if (!activeAccentRgb) {
                const menuElems = Array.from(leftMenu.querySelectorAll("a, button, li, div, span"));
                for (const el of menuElems) {
                    const rect = el.getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) continue;
                    const st = window.getComputedStyle(el);
                    const bgCandidate = parseRgbColor(st.backgroundColor);
                    if (bgCandidate && getSaturation(bgCandidate) > 0.35) {
                        const lum = getLuminance(bgCandidate);
                        if (lum > 0.04 && lum < 0.75) {
                            activeAccentRgb = bgCandidate;
                            break;
                        }
                    }
                }
            }

            const clampChannel = v => Math.min(255, Math.max(0, Math.round(v)));
            const shiftRgb = (rgb, delta) => ({
                r: clampChannel(rgb.r + delta),
                g: clampChannel(rgb.g + delta),
                b: clampChannel(rgb.b + delta)
            });

            // Строим согласованную палитру от цвета левого меню без потери контраста
            const finalBg = isMenuDark
                ? shiftRgb(effectiveMenuBg, -6)
                : shiftRgb(effectiveMenuBg, 4);

            const finalSurface = isMenuDark
                ? shiftRgb(effectiveMenuBg, 10)
                : { r: 255, g: 255, b: 255 };

            const finalText = isMenuDark
                ? { r: 232, g: 234, b: 237 }
                : { r: 32, g: 33, b: 36 };

            const finalPrimary = activeAccentRgb || (isMenuDark
                ? { r: 92, g: 158, b: 255 }
                : { r: 26, g: 115, b: 232 });

            const primaryHover = isMenuDark
                ? shiftRgb(finalPrimary, 22)
                : shiftRgb(finalPrimary, -20);

            return {
                mode: isMenuDark ? "dark" : "light",
                vars: {
                    "--bg": rgbToCss(finalBg),
                    "--surface": rgbToCss(finalSurface),
                    "--text": rgbToCss(finalText),
                    "--primary": rgbToCss(finalPrimary),
                    "--primary-hover": rgbToCss(primaryHover),
                    "--primary-soft": rgbToRgba(finalPrimary, isMenuDark ? 0.22 : 0.14),
                    "--on-primary": getLuminance(finalPrimary) > 0.45 ? "#111318" : "#ffffff"
                }
            };
        } catch {
            return null;
        }
    }

    async function getSettings() {
        try {
            if (!chrome?.storage?.local) return { ...DEFAULT_SETTINGS };
            const data = await chrome.storage.local.get({ settings: DEFAULT_SETTINGS });
            return { ...DEFAULT_SETTINGS, ...(data.settings || {}) };
        } catch {
            return { ...DEFAULT_SETTINGS };
        }
    }

    function sendPanelUpdate(data) {
        try {
            chrome.runtime.sendMessage({ target: "sidepanel", ...data }).catch(() => {});
        } catch {}
    }

    function detectJournalContext() {
        const classSelector = document.querySelector('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]');
        const hasClassSelector = Boolean(classSelector);
        const hasStudentRows = document.querySelectorAll("tbody span[title]").length > 0;
        const onJournalPath =
            window.location.hostname === "school.mos.ru" &&
            (window.location.pathname.includes("/journal") || window.location.pathname.includes("/grade"));

        const isClassJournal = hasClassSelector || hasStudentRows || onJournalPath;

        return {
            isJournalPage: onJournalPath,
            isClassJournal,
            className: hasClassSelector ? classSelector.textContent.trim() : "",
            journalTheme: isClassJournal ? extractJournalTheme() : null
        };
    }

    let contextCheckTimers = [];

    function clearContextCheckTimers() {
        contextCheckTimers.forEach(id => clearTimeout(id));
        contextCheckTimers = [];
    }

    function reportJournalContext(withRetries = false) {
        clearContextCheckTimers();

        const sendCurrent = () => {
            sendPanelUpdate({
                type: "page_context",
                ...detectJournalContext()
            });
        };

        sendCurrent();

        if (withRetries) {
            [600, 1400, 2500].forEach(ms => {
                const timerId = setTimeout(() => {
                    sendCurrent();
                }, ms);
                contextCheckTimers.push(timerId);
            });
        }
    }

    // =========================================================================
    // 1. ЕДИНЫЙ АЛГОРИТМ РАСЧЁТА УЧЕБНЫХ УМЕНИЙ
    // =========================================================================

    function calculateAnswers(stats, settings = DEFAULT_SETTINGS, questionGroups = STANDARD_QUESTIONS) {
        const {
            average,
            gradesCount,
            hwRatio,
            absenceRatio,
            unexcusedRatio,
            isUnstable,
            importantAvg
        } = stats;

        const high = settings.highThreshold ?? 4.5;
        const mid = settings.midThreshold ?? 3.5;
        const low = settings.lowThreshold ?? 2.5;
        const absLimit = settings.absenceRatio ?? 0.5;

        const answers = [];
        const hasManyAbsences = absenceRatio > absLimit;
        const hasEvaluatableGrades = gradesCount > 0 && average > low;

        if (hasManyAbsences && !hasEvaluatableGrades) {
            questionGroups.forEach(group => {
                group.questions.forEach(q => {
                    answers.push({ question_id: String(q.question_id), answer_id: 5 });
                });
            });
            return answers;
        }

        questionGroups.forEach(group => {
            const groupName = (group.question_group_name || "").toLowerCase();

            group.questions.forEach(q => {
                if (hasManyAbsences && (groupName.includes("саморегуляц") || groupName.includes("коммуникац"))) {
                    answers.push({ question_id: String(q.question_id), answer_id: 5 });
                    return;
                }

                let base = average > high ? 4 : (average > mid ? 3 : (average > low ? 2 : 1));

                if (groupName.includes("самоорганизац")) {
                    if (hwRatio >= 0.8 && !isUnstable) base = average > mid ? 4 : Math.min(base + 1, 3);
                    else if (hwRatio <= 0.4) base = Math.min(base, 2);
                    if (isUnstable && base > 2 && Math.random() < 0.5) base -= 1;

                } else if (groupName.includes("самообразован")) {
                    if (importantAvg > high && average > high) base = 4;
                    else if (importantAvg <= mid) base = Math.min(base, 2);
                    else if (importantAvg < (high - 0.3) && base === 4) base = 3;

                } else if (groupName.includes("саморегуляц")) {
                    if (isUnstable && base > 2) base -= 1;
                    if (unexcusedRatio >= 0.25 && base > 2) base -= 1;

                } else {
                    if (gradesCount >= 5 && average > mid && base < 4 && Math.random() < 0.4) {
                        base += 1;
                    } else if (gradesCount <= 2 && base > 2 && Math.random() < 0.3) {
                        base -= 1;
                    }
                }

                if (Math.random() < 0.1) {
                    if (base === 4) base = 3;
                    else if (base === 3) base = Math.random() < 0.5 ? 2 : 4;
                }

                answers.push({
                    question_id: String(q.question_id),
                    answer_id: base
                });
            });
        });

        return answers;
    }

    // =========================================================================
    // 2. УТИЛИТЫ API И ПЕРЕКЛЮЧЕНИЯ КЛАССОВ
    // =========================================================================

    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? decodeURIComponent(match[2]) : null;
    }

    function getApiHeaders() {
        const token = getCookie('aupd_token');
        const profileId = getCookie('profile_id');
        const aid = getCookie('aid') || '14';
        const subsystemId = getCookie('subsystem_id') || '9';

        if (!token || !profileId) {
            throw new Error("Не найдены данные авторизации (aupd_token / profile_id). Обновите страницу журнала.");
        }

        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            "profile-id": profileId,
            "aid": aid,
            "x-mes-subsystem": "teacherweb",
            "x-mes-hostid": subsystemId,
            "x-mes-roleid": subsystemId
        };
    }

    async function apiFetch(url, options = {}) {
        const headers = getApiHeaders();
        if (!options.body) {
            delete headers["Content-Type"];
        }
        const res = await fetch(url, {
            ...options,
            headers: { ...headers, ...(options.headers || {}) },
            credentials: "include"
        });
        if (!res.ok) {
            const errText = await res.text().catch(() => "");
            throw new Error(`Ошибка API ${res.status} (${url}) ${errText}`);
        }
        return res.json();
    }

    function getGroupIdFromUrl() {
        const urlMatch = window.location.href.match(/(?:\/grade\/|\/journal\/|group_id[s]?=)(\d+)/);
        if (urlMatch) return urlMatch[1];

        const resources = performance.getEntriesByType('resource');
        for (let i = resources.length - 1; i >= 0; i--) {
            const match = resources[i].name.match(/group_id[s]?=(\d+)/);
            if (match) return match[1];
        }
        return null;
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
        await delay(3000);
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
            await delay(3000);
            return true;
        }

        document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
        return false;
    }

    // =========================================================================
    // 3. РЕЖИМ 1: ФОНОВЫЙ (ЧЕРЕЗ API)
    // =========================================================================

    async function processClassAPI(forceRecalc, currentClassName, settings) {
        const groupId = getGroupIdFromUrl();
        if (!groupId) {
            throw new Error("Не удалось определить ID группы из адресной строки.");
        }

        const aid = getCookie('aid') || '14';
        sendPanelUpdate({ type: "progress", className: currentClassName, studentName: "Загрузка списка класса...", current: 0, total: 0 });

        const studentsUrl = `https://school.mos.ru/api/ej/core/teacher/v1/student_profiles?academic_year_id=${aid}&group_ids=${groupId}&with_groups=true&with_deleted=false&with_transferred=false&per_page=150&page=1`;
        const students = await apiFetch(studentsUrl);

        if (!Array.isArray(students) || students.length === 0) {
            return { processed: 0, alreadySet: 0, skipped: 0, aborted: false };
        }

        const firstStudent = students[0];
        const groupObj = (firstStudent.groups || []).find(g => String(g.id) === String(groupId));
        if (!groupObj) {
            throw new Error("Не удалось найти метаданные предмета для группы " + groupId);
        }

        const subjectId = groupObj.subject_id;
        const classLevelId = firstStudent.class_unit?.class_level_id || firstStudent.class_level;
        const schoolId = firstStudent.school_id;
        const educationLevelId = firstStudent.education_level || 2;
        const beginDate = groupObj.begin_date || "01.09.2026";
        const endDate = groupObj.end_date || "31.08.2027";

        const marksUrl = `https://school.mos.ru/api/ej/core/teacher/v1/marks?group_ids=${groupId}&subject_id=${subjectId}&class_level_id=${classLevelId}&lesson_date_from=${beginDate}&lesson_date_to=${endDate}&with_non_numeric_entries=true&per_page=1000&page=1`;
        const attendancesUrl = `https://school.mos.ru/api/ej/core/teacher/v1/attendances?group_ids=${groupId}&class_level_id=${classLevelId}&academic_year_id=${aid}&start_at=${beginDate}&stop_at=${endDate}&page=1&per_page=1000`;
        const controlFormsUrl = `https://school.mos.ru/api/ej/core/teacher/v1/control_forms?academic_year_id=${aid}&school_id=${schoolId}&subject_id=${subjectId}&with_grade_system=true&with_deleted=false&education_level_id=${educationLevelId}&page=1&per_page=1000`;

        const [marks, attendances, controlForms] = await Promise.all([
            apiFetch(marksUrl),
            apiFetch(attendancesUrl),
            apiFetch(controlFormsUrl)
        ]);

        const hwControlFormIds = new Set();
        const importantControlFormIds = new Set();

        (controlForms || []).forEach(cf => {
            const name = (cf.name || cf.short_name || "").toLowerCase();
            if (name.includes("цдз") || name.includes("цифров")) hwControlFormIds.add(cf.id);
            if (IMPORTANT_KEYWORDS.some(kw => name.includes(kw))) importantControlFormIds.add(cf.id);
        });

        const allLessonIds = new Set();
        (marks || []).forEach(m => { if (m.schedule_lesson_id) allLessonIds.add(m.schedule_lesson_id); });
        (attendances || []).forEach(a => { if (a.schedule_lesson_id) allLessonIds.add(a.schedule_lesson_id); });
        const totalLessons = allLessonIds.size;

        let processedCount = 0;
        let alreadySetCount = 0;
        let skippedCount = 0;

        for (let i = 0; i < students.length; i++) {
            if (window.meshRobotStopRequested) {
                return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: true };
            }

            const student = students[i];
            const studentName = student.short_name || student.user_name || `Ученик #${i + 1}`;
            sendPanelUpdate({
                type: "progress",
                className: currentClassName,
                studentName,
                current: i + 1,
                total: students.length
            });

            if (!student.person_id) {
                skippedCount++;
                continue;
            }

            const periodsData = await apiFetch(`https://school.mos.ru/api/soft_skills/v1/periods?student_person_id=${student.person_id}`);
            const currentPeriod = (periodsData.periods || []).find(p => p.is_current);

            if (!currentPeriod) {
                skippedCount++;
                continue;
            }

            if (currentPeriod.exist_teacher_answer && !forceRecalc) {
                alreadySetCount++;
                continue;
            }

            const studentMarks = (marks || []).filter(m => m.student_profile_id === student.id && !m.deleted_by);
            const studentAttendances = (attendances || []).filter(a => a.student_profile_id === student.id);

            let grades = [];
            let weightedSum = 0;
            let totalWeight = 0;
            let importantGrades = [];
            let hwTotal = 0;
            let hwCompleted = 0;

            studentMarks.forEach(m => {
                const numericVal = m.values?.[0]?.grade?.five;
                const weight = m.weight || 1;
                const isHw = hwControlFormIds.has(m.control_form_id);
                const isImportant = weight > 1 || importantControlFormIds.has(m.control_form_id);

                if (isHw) {
                    hwTotal++;
                    if (numericVal != null) hwCompleted++;
                }

                if (numericVal != null) {
                    grades.push(numericVal);
                    weightedSum += numericVal * weight;
                    totalWeight += weight;
                    if (isImportant) importantGrades.push(numericVal);
                }
            });

            const totalAbsences = studentAttendances.length;
            const unexcusedAbsences = studentAttendances.filter(a => a.absence_reason_id === 2 || !a.nonattendance_reason_id).length;

            if (grades.length === 0 && totalAbsences === 0) {
                skippedCount++;
                continue;
            }

            const average = totalWeight > 0 ? (weightedSum / totalWeight) : 0;
            const hwRatio = hwTotal > 0 ? (hwCompleted / hwTotal) : 1.0;
            const absenceRatio = totalLessons > 0 ? (totalAbsences / totalLessons) : 0;
            const unexcusedRatio = totalLessons > 0 ? (unexcusedAbsences / totalLessons) : 0;
            const hasTwos = grades.some(g => g <= 2);
            const spread = grades.length > 1 ? (Math.max(...grades) - Math.min(...grades)) : 0;
            const isUnstable = hasTwos || spread >= 2;
            const importantAvg = importantGrades.length > 0
                ? importantGrades.reduce((a, b) => a + b, 0) / importantGrades.length
                : average;

            const answers = calculateAnswers({
                average,
                gradesCount: grades.length,
                hwRatio,
                absenceRatio,
                unexcusedRatio,
                isUnstable,
                importantAvg
            }, settings, STANDARD_QUESTIONS);

            await apiFetch("https://school.mos.ru/api/soft_skills/v1/survey", {
                method: "POST",
                body: JSON.stringify({
                    student_person_id: student.person_id,
                    period_id: currentPeriod.period_id,
                    answers
                })
            });

            console.log(`[МЭШ Ассистент] Выставлено: ${studentName} (ср. ${average.toFixed(2)}, пропуски ${(absenceRatio * 100).toFixed(0)}%)`);
            processedCount++;
            await delay(250);
        }

        return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: false };
    }

    // =========================================================================
    // 4. РЕЖИМ 2: В РЕАЛЬНОМ ВРЕМЕНИ (КЛИКИ ПО ИНТЕРФЕЙСУ)
    // =========================================================================

    async function processClassUI(forceRecalc, currentClassName, settings) {
        let studentSpans = document.querySelectorAll("tbody span[title]");
        if (studentSpans.length === 0) {
            return { processed: 0, alreadySet: 0, skipped: 0, aborted: false };
        }

        let allLessonIds = new Set();
        let hwLessonIds = [];
        let importantLessonIds = [];

        Array.from(document.querySelectorAll('th')).forEach(header => {
            let text = header.textContent.toLowerCase();
            let div = header.querySelector('div[data-test-component]');
            if (!div) return;

            let attr = div.getAttribute("data-test-component");
            let parts = attr.split("_");
            if (parts.length < 2) return;

            let match = parts[0].match(/\d+/);
            if (!match) return;
            let lessonId = match[0];

            allLessonIds.add(lessonId);
            if (text.includes("цдз")) hwLessonIds.push(lessonId);
            if (IMPORTANT_KEYWORDS.some(kw => text.includes(kw))) importantLessonIds.push(lessonId);
        });

        let totalLessons = allLessonIds.size;
        let alreadySetCount = 0;
        let processedCount = 0;
        let skippedCount = 0;

        for (let i = 0; i < studentSpans.length; i++) {
            if (window.meshRobotStopRequested) {
                return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: true };
            }

            let span = studentSpans[i];
            let studentName = span.getAttribute("title") || span.textContent.trim();

            sendPanelUpdate({
                type: "progress",
                className: currentClassName,
                studentName,
                current: i + 1,
                total: studentSpans.length
            });

            let row = span.closest('tr');
            if (!row) {
                skippedCount++;
                continue;
            }

            let cells = row.querySelectorAll('td');
            let gradeText = cells[cells.length - 1].textContent.trim().replace(',', '.');
            let grade = (gradeText && gradeText !== "-") ? parseFloat(gradeText) : 0;

            let grades = [];
            let importantGrades = [];
            let hwCompleted = 0;
            let unexcusedAbsences = 0;
            let totalAbsences = 0;

            let markDivs = row.querySelectorAll('div[data-test-component^="markCell-"]');
            markDivs.forEach(div => {
                let text = div.textContent.trim();
                let lowerText = text.toLowerCase();
                let hasGrade = ['5', '4', '3', '2', '1'].includes(text);

                if (hasGrade) {
                    grades.push(parseInt(text, 10));
                } else if (['н', 'нв'].includes(lowerText)) {
                    unexcusedAbsences++;
                    totalAbsences++;
                } else if (['нб', 'б', 'у'].includes(lowerText)) {
                    totalAbsences++;
                }

                let attr = div.getAttribute("data-test-component");
                if (attr) {
                    let parts = attr.split("_");
                    if (parts.length >= 3) {
                        let lessonId = parts[1];
                        if (hwLessonIds.includes(lessonId)) {
                            if (hasGrade || (text !== "" && !['н', 'нб', 'нв', 'б', 'у'].includes(lowerText))) {
                                hwCompleted++;
                            }
                        }
                        if (hasGrade && importantLessonIds.includes(lessonId)) {
                            importantGrades.push(parseInt(text, 10));
                        }
                    }
                }
            });

            if (grades.length === 0 && totalAbsences === 0) {
                skippedCount++;
                continue;
            }

            let hwRatio = hwLessonIds.length > 0 ? hwCompleted / hwLessonIds.length : 1.0;
            let absenceRatio = totalLessons > 0 ? totalAbsences / totalLessons : 0;
            let unexcusedRatio = totalLessons > 0 ? unexcusedAbsences / totalLessons : 0;
            let hasTwos = grades.includes(2) || grades.includes(1);
            let spread = grades.length > 1 ? Math.max(...grades) - Math.min(...grades) : 0;
            let isUnstable = hasTwos || spread >= 2;
            let importantAvg = importantGrades.length > 0
                ? importantGrades.reduce((a, b) => a + b, 0) / importantGrades.length
                : grade;

            let answers = calculateAnswers({
                average: grade,
                gradesCount: grades.length,
                hwRatio,
                absenceRatio,
                unexcusedRatio,
                isUnstable,
                importantAvg
            }, settings, STANDARD_QUESTIONS);

            span.click();
            await delay(800);

            if (window.meshRobotStopRequested) {
                closeStudentModal();
                return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: true };
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
                skippedCount++;
                closeStudentModal();
                await delay(400);
                continue;
            }

            await delay(1500);

            if (window.meshRobotStopRequested) {
                closeStudentModal();
                return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: true };
            }

            let options2 = Array.from(document.querySelectorAll('label')).filter(l => l.textContent.includes('Редко'));
            let numQuestions = Math.min(options2.length, answers.length);

            if (numQuestions === 0) {
                document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', bubbles: true }));
                await delay(400);
                skippedCount++;
                continue;
            }

            for (let q = 0; q < numQuestions; q++) {
                if (q === 0) {
                    let dummys = Array.from(document.querySelectorAll('label')).filter(l => l.textContent.includes('Почти никогда'));
                    if (dummys.length > 0) {
                        dummys[0].click();
                        await delay(150);
                    }
                }

                let targetText = SKILL_LABELS[answers[q].answer_id];
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

            if (window.meshRobotStopRequested) {
                closeStudentModal();
                processedCount++;
                return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: true };
            }

            let closeBtn = getElementByExactText('button', 'Закрыть');
            if (closeBtn) closeBtn.click();

            processedCount++;
            await delay(800);
        }

        return { processed: processedCount, alreadySet: alreadySetCount, skipped: skippedCount, aborted: false };
    }

    // =========================================================================
    // 5. ГЛАВНЫЙ КОНТРОЛЛЕР
    // =========================================================================

    async function runRobot(forceRecalc, processAll, mode = "background") {
        if (window.isMeshRobotRunning) {
            return;
        }

        window.isMeshRobotRunning = true;
        window.meshRobotStopRequested = false;

        let globalStats = { processed: 0, alreadySet: 0, skipped: 0, classes: 0 };

        try {
            const settings = await getSettings();

            if (processAll) {
                sendPanelUpdate({ type: "progress", studentName: "Переход к первому классу..." });
                let switchedToFirst = await switchToFirstClass();
                if (!switchedToFirst || window.meshRobotStopRequested) {
                    if (!window.meshRobotStopRequested) {
                        throw new Error("Не удалось открыть список классов.");
                    }
                    return;
                }
            }

            do {
                if (window.meshRobotStopRequested) break;

                let dropdownWrapper = document.querySelector('[data-test-component="leftControlHeadSelectGroup-selectSingleWrapper"]');
                let currentClass = dropdownWrapper ? dropdownWrapper.textContent.trim() : "Текущий класс";

                let stats = mode === "background"
                    ? await processClassAPI(forceRecalc, currentClass, settings)
                    : await processClassUI(forceRecalc, currentClass, settings);

                globalStats.processed += stats.processed;
                globalStats.alreadySet += stats.alreadySet;
                globalStats.skipped += stats.skipped;
                globalStats.classes++;

                if (stats.aborted || window.meshRobotStopRequested || !processAll) break;

                sendPanelUpdate({ type: "progress", studentName: "Переключаем класс..." });
                let hasNext = await switchNextClass(currentClass);
                if (!hasNext) break;

            } while (true);

            const summaryText =
                `Классов пройдено: ${globalStats.classes}\n` +
                `Успешно выставлено: ${globalStats.processed}\n` +
                `Уже стояли (пропущено): ${globalStats.alreadySet}\n` +
                `Нет данных: ${globalStats.skipped}`;

            if (window.meshRobotStopRequested) {
                sendPanelUpdate({
                    type: "finish",
                    title: "Остановлено пользователем",
                    summary: summaryText,
                    isError: true,
                    showReload: mode === "background" && globalStats.processed > 0
                });
            } else {
                sendPanelUpdate({
                    type: "finish",
                    title: "Готово!",
                    summary: summaryText,
                    isError: false,
                    showReload: mode === "background"
                });
            }
        } catch (err) {
            console.error("[МЭШ Ассистент] Ошибка:", err);
            sendPanelUpdate({
                type: "error",
                title: "Произошла ошибка",
                summary: `${err.message}\n\nПодробности в консоли (F12).`,
                isError: true,
                showReload: false
            });
        } finally {
            window.isMeshRobotRunning = false;
            window.meshRobotStopRequested = false;
        }
    }

    if (!window.meshRobotListenerAdded) {
        window.meshRobotListenerAdded = true;
        chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
            if (request.action === "start") {
                runRobot(request.forceRecalc, request.processAll, request.mode);
            } else if (request.action === "stop") {
                window.meshRobotStopRequested = true;
            } else if (request.action === "check_context") {
                const ctx = detectJournalContext();
                reportJournalContext(true);
                sendResponse?.(ctx);
                return true;
            }
        });
    }

    reportJournalContext(true);
})();