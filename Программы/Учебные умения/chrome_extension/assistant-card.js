export function createAssistantCard({
    id,
    title,
    open = true,
    onTogglePause,
    onStop
}) {
    const section = document.createElement("section");
    section.className = `assistant-accordion${open ? " is-open" : ""}`;
    section.dataset.assistant = id;

    section.innerHTML = `
        <button type="button" class="accordion-header" aria-expanded="${open}">
            <div class="accordion-title-group">
                <span class="accordion-title">${title}</span>
                <span class="accordion-badge" data-role="badge">Готов</span>
            </div>
            <span class="accordion-chevron" aria-hidden="true">▾</span>
        </button>

        <div class="accordion-body">
            <div class="assistant-settings" data-role="settings"></div>

            <div class="assistant-run-box" data-role="runBox">
                <div class="run-box-top">
                    <div class="run-status-wrap">
                        <span class="run-status-text" data-role="statusText">Ожидание запуска</span>
                        <span class="run-sub-text" data-role="subText"></span>
                    </div>

                    <div class="player-controls" role="group" aria-label="Управление выполнением">
                        <button type="button" class="player-btn" data-role="pauseBtn" title="Пауза" aria-label="Пауза" disabled>
                            <svg class="icon-pause" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
                                <rect x="3.5" y="2.5" width="3" height="11" rx="0.8"/>
                                <rect x="9.5" y="2.5" width="3" height="11" rx="0.8"/>
                            </svg>
                            <svg class="icon-play" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true" hidden>
                                <polygon points="4.2,2.6 13.2,8 4.2,13.4"/>
                            </svg>
                        </button>

                        <button type="button" class="player-btn player-btn-stop" data-role="stopBtn" title="Остановить" aria-label="Остановить" disabled>
                            <svg viewBox="0 0 16 16" width="13" height="13" fill="currentColor" aria-hidden="true">
                                <rect x="3.5" y="3.5" width="9" height="9" rx="1.2"/>
                            </svg>
                        </button>
                    </div>
                </div>

                <div class="run-meta-row">
                    <span class="run-current-student" data-role="currentItem">—</span>
                    <span class="run-counter" data-role="counter">0 / 0</span>
                </div>

                <div class="run-progress-track" aria-hidden="true">
                    <div class="run-progress-bar" data-role="progressBar" style="width: 0%;"></div>
                </div>

                <div class="assistant-footer-slot" data-role="footerSlot" hidden></div>
            </div>
        </div>
    `;

    const refs = {
        section,
        header: section.querySelector(".accordion-header"),
        badge: section.querySelector('[data-role="badge"]'),
        settings: section.querySelector('[data-role="settings"]'),
        runBox: section.querySelector('[data-role="runBox"]'),
        statusText: section.querySelector('[data-role="statusText"]'),
        subText: section.querySelector('[data-role="subText"]'),
        pauseBtn: section.querySelector('[data-role="pauseBtn"]'),
        pauseIcon: section.querySelector(".icon-pause"),
        playIcon: section.querySelector(".icon-play"),
        stopBtn: section.querySelector('[data-role="stopBtn"]'),
        currentItem: section.querySelector('[data-role="currentItem"]'),
        counter: section.querySelector('[data-role="counter"]'),
        progressBar: section.querySelector('[data-role="progressBar"]'),
        footerSlot: section.querySelector('[data-role="footerSlot"]')
    };

    let isPaused = false;

    function setOpen(nextOpen) {
        section.classList.toggle("is-open", nextOpen);
        refs.header.setAttribute("aria-expanded", String(nextOpen));
    }

    function setPaused(paused) {
        isPaused = paused;
        refs.pauseBtn.classList.toggle("is-paused", paused);
        refs.pauseBtn.title = paused ? "Продолжить" : "Пауза";
        refs.pauseBtn.setAttribute("aria-label", paused ? "Продолжить" : "Пауза");
        refs.pauseIcon.hidden = paused;
        refs.playIcon.hidden = !paused;
    }

    refs.header.addEventListener("click", () => {
        setOpen(!section.classList.contains("is-open"));
    });

    refs.pauseBtn.addEventListener("click", () => {
        onTogglePause?.(!isPaused);
    });

    refs.stopBtn.addEventListener("click", () => {
        onStop?.();
    });

    function setState(state, payload = {}) {
        refs.badge.className = "accordion-badge";
        refs.runBox.className = "assistant-run-box";

        if (state === "running") {
            setOpen(true);
            setPaused(false);
            refs.pauseBtn.disabled = false;
            refs.stopBtn.disabled = false;
            refs.badge.textContent = "Идёт";
            refs.badge.classList.add("is-running");
            refs.statusText.textContent = payload.statusText || "Обработка...";
        } else if (state === "paused") {
            setPaused(true);
            refs.pauseBtn.disabled = false;
            refs.stopBtn.disabled = false;
            refs.badge.textContent = "Пауза";
            refs.badge.classList.add("is-paused");
            refs.statusText.textContent = payload.statusText || "На паузе";
        } else if (state === "stopped") {
            setPaused(false);
            refs.pauseBtn.disabled = true;
            refs.stopBtn.disabled = true;
            refs.badge.textContent = "Остановлено";
            refs.badge.classList.add("is-stopped");
            refs.runBox.classList.add("is-stopped");
            refs.statusText.textContent = payload.statusText || "Остановлено пользователем";
        } else if (state === "error") {
            setPaused(false);
            refs.pauseBtn.disabled = true;
            refs.stopBtn.disabled = true;
            refs.badge.textContent = "Ошибка";
            refs.badge.classList.add("is-error");
            refs.runBox.classList.add("is-error");
            refs.statusText.textContent = payload.statusText || "Ошибка выполнения";
        } else {
            setPaused(false);
            refs.pauseBtn.disabled = true;
            refs.stopBtn.disabled = true;
            refs.badge.textContent = "Готово";
            refs.statusText.textContent = payload.statusText || "Завершено";
        }

        if (payload.subText !== undefined) refs.subText.textContent = payload.subText;
        if (payload.currentItem !== undefined) refs.currentItem.textContent = payload.currentItem;
        if (payload.current !== undefined && payload.total !== undefined) {
            refs.counter.textContent = `${payload.current} из ${payload.total}`;
            const pct = payload.total > 0 ? Math.min(100, Math.round((payload.current / payload.total) * 100)) : 0;
            refs.progressBar.style.width = `${pct}%`;
        }
    }

    return {
        element: section,
        settingsSlot: refs.settings,
        footerSlot: refs.footerSlot,
        setOpen,
        setState
    };
}