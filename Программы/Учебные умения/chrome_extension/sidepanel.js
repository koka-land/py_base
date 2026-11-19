const DEFAULT_SETTINGS = {
    themeMode: "mesh",
    fontScaleStep: 0,
    highThreshold: 4.5,
    midThreshold: 3.5,
    lowThreshold: 2.5,
    absenceRatio: 0.5
};

const notClassJournalHint = document.getElementById("notClassJournalHint");
const skillsControls = document.getElementById("skillsControls");
const fontScaleSlider = document.getElementById("fontScaleSlider");
const fontScaleBadge = document.getElementById("fontScaleBadge");

const themeAccordionBtn = document.getElementById("themeAccordionBtn");
const themeAccordionBody = document.getElementById("themeAccordionBody");
const fontAccordionBtn = document.getElementById("fontAccordionBtn");
const fontAccordionBody = document.getElementById("fontAccordionBody");
const thresholdsAccordionBtn = document.getElementById("thresholdsAccordionBtn");
const thresholdsAccordionBody = document.getElementById("thresholdsAccordionBody");

const darkSchemeMedia = window.matchMedia("(prefers-color-scheme: dark)");
let currentThemeMode = "mesh";
let contextRetryTimer = null;
let isTaskRunning = false;
let isPanelCollapsed = false;
let lastAppliedClassJournal = null;

function setAccordionOpen(btn, body, open) {
    const isOpen = Boolean(open);
    btn?.setAttribute("aria-expanded", String(isOpen));
    body?.classList.toggle("open", isOpen);
}

themeAccordionBtn?.addEventListener("click", () => {
    const currentlyOpen = themeAccordionBtn.getAttribute("aria-expanded") === "true";
    setAccordionOpen(themeAccordionBtn, themeAccordionBody, !currentlyOpen);
});

fontAccordionBtn?.addEventListener("click", () => {
    const currentlyOpen = fontAccordionBtn.getAttribute("aria-expanded") === "true";
    setAccordionOpen(fontAccordionBtn, fontAccordionBody, !currentlyOpen);
});

thresholdsAccordionBtn?.addEventListener("click", () => {
    const currentlyOpen = thresholdsAccordionBtn.getAttribute("aria-expanded") === "true";
    setAccordionOpen(thresholdsAccordionBtn, thresholdsAccordionBody, !currentlyOpen);
});

function getStepDecimals(stepValue) {
    const str = String(stepValue);
    const dotIndex = str.indexOf(".");
    return dotIndex === -1 ? 0 : str.length - dotIndex - 1;
}

function syncStepperButtons(box) {
    const input = box.querySelector('input[type="number"]');
    const prevBtn = box.querySelector('[data-step-dir="-1"]');
    const nextBtn = box.querySelector('[data-step-dir="1"]');
    if (!input) return;

    const min = input.min !== "" ? parseFloat(input.min) : -Infinity;
    const max = input.max !== "" ? parseFloat(input.max) : Infinity;
    const val = parseFloat(input.value);

    if (Number.isNaN(val)) {
        if (prevBtn) prevBtn.disabled = false;
        if (nextBtn) nextBtn.disabled = false;
        return;
    }

    if (prevBtn) prevBtn.disabled = val <= min;
    if (nextBtn) nextBtn.disabled = val >= max;
}

document.querySelectorAll(".stepper-box").forEach(box => {
    const input = box.querySelector('input[type="number"]');
    if (!input) return;

    box.querySelectorAll(".stepper-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const dir = parseInt(btn.dataset.stepDir, 10) || 0;
            const step = parseFloat(input.step) || 1;
            const min = input.min !== "" ? parseFloat(input.min) : -Infinity;
            const max = input.max !== "" ? parseFloat(input.max) : Infinity;
            const decimals = getStepDecimals(step);

            const current = Number.isNaN(parseFloat(input.value))
                ? (min !== -Infinity ? min : 0)
                : parseFloat(input.value);

            let next = current + dir * step;
            next = Math.min(max, Math.max(min, next));
            next = Number(next.toFixed(decimals));

            input.value = String(next);
            input.dispatchEvent(new Event("change", { bubbles: true }));
            syncStepperButtons(box);
        });
    });

    input.addEventListener("input", () => syncStepperButtons(box));
    input.addEventListener("change", () => syncStepperButtons(box));
    syncStepperButtons(box);
});

function resolveEffectiveTheme(mode) {
    if (mode === "mesh" || mode === "light" || mode === "dark") {
        return mode;
    }
    return darkSchemeMedia.matches ? "dark" : "mesh";
}

function applyThemeMode(mode) {
    const validMode = ["mesh", "light", "dark", "auto"].includes(mode)
        ? (mode === "auto" ? "mesh" : mode)
        : "mesh";
    currentThemeMode = validMode;

    const radio = document.querySelector(`input[name="themeMode"][value="${validMode}"]`);
    if (radio) radio.checked = true;

    document.documentElement.setAttribute("data-theme", resolveEffectiveTheme(validMode));
}

darkSchemeMedia.addEventListener("change", () => {
    if (currentThemeMode === "auto") {
        applyThemeMode("auto");
    }
});

document.querySelectorAll('input[name="themeMode"]').forEach(input => {
    input.addEventListener("change", () => {
        applyThemeMode(input.value);
    });
});

function formatFontStepLabel(step) {
    const n = Math.max(-2, Math.min(2, Number(step) || 0));
    if (n === 0) return "0 (стандарт)";
    return n > 0 ? `+${n}` : `${n}`;
}

function applyFontScaleStep(step) {
    const n = Math.max(-2, Math.min(2, Number(step) || 0));
    document.documentElement.style.setProperty("--font-offset", `${n}px`);
    if (fontScaleSlider) fontScaleSlider.value = String(n);
    if (fontScaleBadge) fontScaleBadge.textContent = formatFontStepLabel(n);
}

fontScaleSlider?.addEventListener("input", () => {
    applyFontScaleStep(fontScaleSlider.value);
});

function applyClassJournalState(isClassJournal) {
    const normalized = Boolean(isClassJournal);
    lastAppliedClassJournal = normalized;

    if (normalized) {
        notClassJournalHint.style.display = "none";
        skillsControls.style.display = "block";
    } else {
        notClassJournalHint.style.display = "block";
        skillsControls.style.display = "none";
        if (!isTaskRunning) {
            hideBottomPanel();
        }
    }
}

function requestPageContextWithRetry(retriesLeft = 3) {
    clearTimeout(contextRetryTimer);

    chrome.runtime.sendMessage({
        target: "content",
        payload: { action: "check_context" }
    }, (res) => {
        if (!chrome.runtime.lastError && res && typeof res.isClassJournal === "boolean") {
            applyClassJournalState(res.isClassJournal);
            return;
        }

        if (chrome.runtime.lastError || !res?.ok) {
            if (retriesLeft > 0) {
                contextRetryTimer = setTimeout(() => {
                    requestPageContextWithRetry(retriesLeft - 1);
                }, 700);
            } else {
                applyClassJournalState(false);
            }
        }
    });
}

document.querySelectorAll(".link-btn[data-url]").forEach(btn => {
    btn.addEventListener("click", () => {
        chrome.runtime.sendMessage({
            action: "open_url",
            url: btn.dataset.url
        });
    });
});

document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

        btn.classList.add("active");
        const targetPane = document.getElementById(`tab-${btn.dataset.tab}`);
        if (targetPane) targetPane.classList.add("active");
    });
});

async function loadSettingsUI() {
    const data = await chrome.storage.local.get({ settings: DEFAULT_SETTINGS });
    const s = { ...DEFAULT_SETTINGS, ...(data.settings || {}) };

    applyThemeMode(s.themeMode ?? "mesh");
    applyFontScaleStep(s.fontScaleStep ?? 0);
    document.getElementById("highThreshold").value = s.highThreshold;
    document.getElementById("midThreshold").value = s.midThreshold;
    document.getElementById("lowThreshold").value = s.lowThreshold;
    document.getElementById("absenceThreshold").value = Math.round((s.absenceRatio ?? 0.5) * 100);

    document.querySelectorAll(".stepper-box").forEach(syncStepperButtons);
}

loadSettingsUI();
requestPageContextWithRetry();

document.getElementById("saveSettingsBtn").addEventListener("click", async () => {
    const themeMode = document.querySelector('input[name="themeMode"]:checked')?.value || "mesh";
    const fontScaleStep = Math.max(-2, Math.min(2, parseInt(fontScaleSlider.value, 10) || 0));
    const highThreshold = parseFloat(document.getElementById("highThreshold").value) || 4.5;
    const midThreshold = parseFloat(document.getElementById("midThreshold").value) || 3.5;
    const lowThreshold = parseFloat(document.getElementById("lowThreshold").value) || 2.5;
    const absencePct = Math.min(95, Math.max(10, parseFloat(document.getElementById("absenceThreshold").value) || 50));

    const settings = {
        themeMode,
        fontScaleStep,
        highThreshold,
        midThreshold,
        lowThreshold,
        absenceRatio: absencePct / 100
    };

    await chrome.storage.local.set({ settings });

    const statusEl = document.getElementById("saveStatus");
    statusEl.textContent = "Настройки сохранены";
    setTimeout(() => { statusEl.textContent = ""; }, 2000);
});

document.getElementById("resetSettingsBtn").addEventListener("click", async () => {
    await chrome.storage.local.set({ settings: DEFAULT_SETTINGS });
    await loadSettingsUI();
    setAccordionOpen(themeAccordionBtn, themeAccordionBody, false);
    setAccordionOpen(fontAccordionBtn, fontAccordionBody, false);
    setAccordionOpen(thresholdsAccordionBtn, thresholdsAccordionBody, false);

    const statusEl = document.getElementById("saveStatus");
    statusEl.textContent = "Сброшено по умолчанию";
    setTimeout(() => { statusEl.textContent = ""; }, 2000);
});

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const reloadBtn = document.getElementById("reloadBtn");

const bottomPanel = document.getElementById("bottomPanel");
const panelStatus = document.getElementById("panelStatus");
const panelCollapsibleBody = document.getElementById("panelCollapsibleBody");
const panelClass = document.getElementById("panelClass");
const panelStudent = document.getElementById("panelStudent");
const panelCounter = document.getElementById("panelCounter");
const panelBar = document.getElementById("panelBar");
const panelSummary = document.getElementById("panelSummary");
const panelActions = document.getElementById("panelActions");
const toggleCollapsePanelBtn = document.getElementById("toggleCollapsePanelBtn");

function applyPanelCollapseState(collapsed) {
    isPanelCollapsed = Boolean(collapsed);
    bottomPanel.classList.toggle("collapsed", isPanelCollapsed);
    if (panelCollapsibleBody) {
        panelCollapsibleBody.style.display = isPanelCollapsed ? "none" : "block";
    }
    if (toggleCollapsePanelBtn) {
        toggleCollapsePanelBtn.setAttribute("aria-expanded", String(!isPanelCollapsed));
        toggleCollapsePanelBtn.textContent = isPanelCollapsed ? "▴" : "▾";
        toggleCollapsePanelBtn.title = isPanelCollapsed ? "Развернуть" : "Свернуть";
        toggleCollapsePanelBtn.setAttribute(
            "aria-label",
            isPanelCollapsed ? "Развернуть блок выполнения" : "Свернуть блок выполнения"
        );
    }
}

toggleCollapsePanelBtn?.addEventListener("click", () => {
    applyPanelCollapseState(!isPanelCollapsed);
});

function setRunningState(running) {
    isTaskRunning = running;
    startBtn.style.display = running ? "none" : "";
    startBtn.disabled = running;

    if (stopBtn) {
        stopBtn.style.display = running ? "inline-flex" : "none";
        stopBtn.disabled = !running;
    }
}

function setPanelBorder(variant) {
    bottomPanel.classList.remove("neutral", "success", "error");
    bottomPanel.classList.add("visible", variant);
}

function hideBottomPanel() {
    bottomPanel.classList.remove("visible", "neutral", "success", "error", "collapsed");
    isPanelCollapsed = false;
    if (panelCollapsibleBody) {
        panelCollapsibleBody.style.display = "block";
    }
    if (toggleCollapsePanelBtn) {
        toggleCollapsePanelBtn.setAttribute("aria-expanded", "true");
        toggleCollapsePanelBtn.textContent = "▾";
        toggleCollapsePanelBtn.title = "Свернуть";
    }
    if (stopBtn) {
        stopBtn.style.display = "none";
        stopBtn.disabled = true;
    }
    panelSummary.classList.remove("visible");
    panelSummary.textContent = "";
    panelActions.classList.remove("visible");
}

startBtn.addEventListener("click", () => {
    const mode = document.querySelector('input[name="mode"]:checked')?.value || "background";
    const forceRecalc = document.getElementById("forceRecalc").checked;
    const processAll = document.getElementById("processAll").checked;

    applyPanelCollapseState(false);
    setPanelBorder("neutral");
    panelStatus.textContent = "Обработка...";
    panelClass.textContent = "Подготовка...";
    panelStudent.textContent = "Запуск...";
    panelCounter.textContent = "0 из 0";
    panelBar.style.width = "0%";
    panelSummary.classList.remove("visible");
    panelSummary.textContent = "";
    panelActions.classList.remove("visible");
    setRunningState(true);

    chrome.runtime.sendMessage({
        target: "content",
        payload: {
            action: "start",
            mode,
            forceRecalc,
            processAll
        }
    });
});

stopBtn?.addEventListener("click", () => {
    stopBtn.disabled = true;
    panelStatus.textContent = "Остановка...";
    chrome.runtime.sendMessage({
        target: "content",
        payload: { action: "stop" }
    });
});

reloadBtn.addEventListener("click", () => {
    hideBottomPanel();
    chrome.runtime.sendMessage({ action: "reload_active_tab" });
});

chrome.runtime.onMessage.addListener((msg) => {
    if (msg?.target !== "sidepanel") return;

    if (msg.type === "page_context") {
        clearTimeout(contextRetryTimer);
        if (msg.isClassJournal) {
            applyClassJournalState(true);
        } else if (msg.isJournalPage) {
            contextRetryTimer = setTimeout(() => {
                requestPageContextWithRetry(1);
            }, 800);
            if (lastAppliedClassJournal === null) {
                applyClassJournalState(false);
            }
        } else {
            applyClassJournalState(false);
        }
        return;
    }

    if (msg.type === "context_changed") {
        clearTimeout(contextRetryTimer);
        if (!msg.isJournal) {
            applyClassJournalState(false);
        } else {
            requestPageContextWithRetry(3);
        }
        return;
    }

    if (msg.type === "progress") {
        setPanelBorder("neutral");
        panelStatus.textContent = "Обработка...";
        if (msg.className !== undefined) panelClass.textContent = msg.className;
        if (msg.studentName !== undefined) panelStudent.textContent = msg.studentName;
        if (msg.current !== undefined && msg.total !== undefined) {
            panelCounter.textContent = `${msg.current} из ${msg.total}`;
            const pct = msg.total > 0 ? Math.min(100, Math.round((msg.current / msg.total) * 100)) : 0;
            panelBar.style.width = `${pct}%`;
        }
    } else if (msg.type === "finish" || msg.type === "error") {
        setRunningState(false);
        applyPanelCollapseState(false);
        const isErr = Boolean(msg.isError || msg.type === "error");

        setPanelBorder(isErr ? "error" : "success");
        panelStatus.textContent = msg.title || (isErr ? "Ошибка" : "Готово!");
        if (!isErr) panelBar.style.width = "100%";

        panelSummary.textContent = msg.summary || "";
        panelSummary.classList.add("visible");

        if (msg.showReload) {
            panelActions.classList.add("visible");
        } else {
            panelActions.classList.remove("visible");
        }
    }
});