function createAssistantCard({
    id,
    title,
    open = true,
    onTogglePause,
    onStop,
    onReload
}) {
    const card = document.createElement("section");
    card.className = `assistant-card${open ? " is-open" : ""}`;
    card.dataset.assistant = id;

    card.innerHTML = `
        <button type="button" class="assistant-card-header" aria-expanded="${open}">
            <span class="assistant-card-title-wrap">
                <span class="assistant-card-title">${title}</span>
                <span class="assistant-card-badge" data-role="badge">Готов</span>
            </span>
            <span class="assistant-card-chevron" aria-hidden="true">▾</span>
        </button>

        <div class="assistant-card-body">
            <div class="assistant-settings-slot" data-role="settingsSlot"></div>

            <div class="assistant-run-panel neutral" data-role="runPanel">
                <div class="run-top-row">
                    <span class="run-status" data-role="status">Ожидание</span>
                    <div class="run-controls">
                        <button type="button" class="player-btn" data-role="pauseBtn" title="Пауза" aria-label="Пауза" disabled>
                            <svg class="icon-pause" viewBox="0 0 16 16" width="13" height="13" fill="currentColor" aria-hidden="true">
                                <rect x="3.5" y="2.5" width="3" height="11" rx="0.8"/>
                                <rect x="9.5" y="2.5" width="3" height="11" rx="0.8"/>
                            </svg>
                            <svg class="icon-play" viewBox="0 0 16 16" width="13" height="13" fill="currentColor" aria-hidden="true" hidden>
                                <polygon points="4.2,2.6 13.2,8 4.2,13.4"/>
                            </svg>
                        </button>
                        <button type="button" class="player-btn player-btn-stop" data-role="stopBtn" title="Остановить" aria-label="Остановить" disabled>
                            <svg viewBox="0 0 16 16" width="12" height="12" fill="currentColor" aria-hidden="true">
                                <rect x="3.5" y="3.5" width="9" height="9" rx="1.2"/>
                            </svg>
                        </button>
                        <button type="button" class="panel-collapse-btn" data-role="collapseBtn" aria-expanded="true" title="Свернуть">▾</button>
                    </div>
                </div>

                <div class="run-details" data-role="details">
                    <div class="run-class" data-role="className">Подготовка...</div>
                    <div class="panel-meta">
                        <span class="panel-student" data-role="studentName">—</span>
                        <span class="panel-counter" data-role="counter">0 из 0</span>
                    </div>
                </div>

                <div class="bar-track">
                    <div class="bar-fill" data-role="barFill" style="width: 0%;"></div>
                </div>

                <div class="panel-summary" data-role="summary"></div>
                <div class="panel-actions" data-role="actions">
                    <button type="button" class="btn btn-secondary" data-role="reloadBtn" style="width:100%;">
                        Обновить страницу
                    </button>
                </div>
                <div class="assistant-report-slot" data-role="reportSlot"></div>
            </div>
        </div>
    `;

    const refs = {
        card,
        header: card.querySelector(".assistant-card-header"),
        badge: card.querySelector('[data-role="badge"]'),
        settingsSlot: card.querySelector('[data-role="settingsSlot"]'),
        runPanel: card.querySelector('[data-role="runPanel"]'),
        status: card.querySelector('[data-role="status"]'),
        pauseBtn: card.querySelector('[data-role="pauseBtn"]'),
        pauseIcon: card.querySelector(".icon-pause"),
        playIcon: card.querySelector(".icon-play"),
        stopBtn: card.querySelector('[data-role="stopBtn"]'),
        collapseBtn: card.querySelector('[data-role="collapseBtn"]'),
        details: card.querySelector('[data-role="details"]'),
        className: card.querySelector('[data-role="className"]'),
        studentName: card.querySelector('[data-role="studentName"]'),
        counter: card.querySelector('[data-role="counter"]'),
        barFill: card.querySelector('[data-role="barFill"]'),
        summary: card.querySelector('[data-role="summary"]'),
        actions: card.querySelector('[data-role="actions"]'),
        reloadBtn: card.querySelector('[data-role="reloadBtn"]'),
        reportSlot: card.querySelector('[data-role="reportSlot"]')
    };

    let isPaused = false;
    let isCollapsed = false;

    function setOpen(nextOpen) {
        const val = Boolean(nextOpen);
        card.classList.toggle("is-open", val);
        refs.header.setAttribute("aria-expanded", String(val));
    }

    function setPaused(paused) {
    isPaused = Boolean(paused);
    refs.pauseBtn.classList.toggle("is-paused", isPaused);
    refs.pauseBtn.title = isPaused ? "Продолжить" : "Пауза";
    refs.pauseBtn.setAttribute("aria-label", isPaused ? "Продолжить" : "Пауза");
    if (refs.pauseIcon) refs.pauseIcon.style.display = isPaused ? "none" : "block";
    if (refs.playIcon) refs.playIcon.style.display = isPaused ? "block" : "none";
}

    function setCollapsed(collapsed) {
    isCollapsed = Boolean(collapsed);
    refs.details.style.display = isCollapsed ? "none" : "block";
    refs.collapseBtn.setAttribute("aria-expanded", String(!isCollapsed));
    refs.collapseBtn.textContent = isCollapsed ? "▾" : "▴";
    refs.collapseBtn.title = isCollapsed ? "Развернуть" : "Свернуть";
}

    refs.header.addEventListener("click", () => {
        setOpen(!card.classList.contains("is-open"));
    });

    refs.pauseBtn.addEventListener("click", () => {
        onTogglePause?.(!isPaused);
    });

    refs.stopBtn.addEventListener("click", () => {
        refs.pauseBtn.disabled = true;
        refs.stopBtn.disabled = true;
        refs.status.textContent = "Остановка...";
        onStop?.();
    });

    refs.collapseBtn.addEventListener("click", () => {
        setCollapsed(!isCollapsed);
    });

    refs.reloadBtn.addEventListener("click", () => {
        onReload?.();
    });

    function showRunPanel(variant = "neutral") {
        refs.runPanel.classList.remove("neutral", "success", "error");
        refs.runPanel.classList.add("visible", variant);
    }

    function hideRunPanel() {
        refs.runPanel.classList.remove("visible", "neutral", "success", "error");
        refs.summary.classList.remove("visible");
        refs.summary.textContent = "";
        refs.actions.classList.remove("visible");
        refs.barFill.style.width = "0%";
        setPaused(false);
        setCollapsed(false);
        refs.pauseBtn.disabled = true;
        refs.stopBtn.disabled = true;
        refs.badge.className = "assistant-card-badge";
        refs.badge.textContent = "Готов";
    }

    function setRunning(running) {
        refs.pauseBtn.disabled = !running;
        refs.stopBtn.disabled = !running;
        if (running) {
            setOpen(true);
            setPaused(false);
            refs.badge.className = "assistant-card-badge is-running";
            refs.badge.textContent = "Идёт";
        }
    }

    function setPausedState(paused, statusText = "На паузе") {
        setPaused(paused);
        refs.badge.className = paused ? "assistant-card-badge is-paused" : "assistant-card-badge is-running";
        refs.badge.textContent = paused ? "Пауза" : "Идёт";
        refs.status.textContent = paused ? statusText : "Обработка...";
    }

    return {
        element: card,
        refs,
        setOpen,
        setCollapsed,
        showRunPanel,
        hideRunPanel,
        setRunning,
        setPausedState
    };
}