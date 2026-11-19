const DEFAULT_SETTINGS = {
    highThreshold: 4.5,
    midThreshold: 3.5,
    lowThreshold: 2.5,
    absenceRatio: 0.5
};

// Переключение вкладок
document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

        btn.classList.add("active");
        document.getElementById(`tab-${btn.dataset.tab}`).classList.add("active");
    });
});

// Загрузка настроек в форму
async function loadSettingsUI() {
    const data = await chrome.storage.local.get({ settings: DEFAULT_SETTINGS });
    const s = { ...DEFAULT_SETTINGS, ...(data.settings || {}) };

    document.getElementById("highThreshold").value = s.highThreshold;
    document.getElementById("midThreshold").value = s.midThreshold;
    document.getElementById("lowThreshold").value = s.lowThreshold;
    document.getElementById("absenceThreshold").value = Math.round((s.absenceRatio ?? 0.5) * 100);
}

loadSettingsUI();

// Сохранение настроек
document.getElementById("saveSettingsBtn").addEventListener("click", async () => {
    const highThreshold = parseFloat(document.getElementById("highThreshold").value) || 4.5;
    const midThreshold = parseFloat(document.getElementById("midThreshold").value) || 3.5;
    const lowThreshold = parseFloat(document.getElementById("lowThreshold").value) || 2.5;
    const absencePct = Math.min(95, Math.max(10, parseFloat(document.getElementById("absenceThreshold").value) || 50));

    const settings = {
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

// Сброс настроек
document.getElementById("resetSettingsBtn").addEventListener("click", async () => {
    await chrome.storage.local.set({ settings: DEFAULT_SETTINGS });
    await loadSettingsUI();

    const statusEl = document.getElementById("saveStatus");
    statusEl.textContent = "Сброшено по умолчанию";
    setTimeout(() => { statusEl.textContent = ""; }, 2000);
});

// Элементы управления и нижнего блока
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const reloadBtn = document.getElementById("reloadBtn");

const bottomPanel = document.getElementById("bottomPanel");
const panelStatus = document.getElementById("panelStatus");
const panelClass = document.getElementById("panelClass");
const panelStudent = document.getElementById("panelStudent");
const panelCounter = document.getElementById("panelCounter");
const panelBar = document.getElementById("panelBar");
const panelSummary = document.getElementById("panelSummary");
const panelActions = document.getElementById("panelActions");
const dismissPanelBtn = document.getElementById("dismissPanelBtn");

function setRunningState(running) {
    startBtn.disabled = running;
    stopBtn.disabled = !running;
}

function setPanelBorder(variant) {
    bottomPanel.classList.remove("neutral", "success", "error");
    bottomPanel.classList.add("visible", variant);
}

function hideBottomPanel() {
    bottomPanel.classList.remove("visible", "neutral", "success", "error");
    panelSummary.classList.remove("visible");
    panelSummary.textContent = "";
    panelActions.classList.remove("visible");
}

dismissPanelBtn.addEventListener("click", hideBottomPanel);

startBtn.addEventListener("click", () => {
    const mode = document.querySelector('input[name="mode"]:checked')?.value || "background";
    const forceRecalc = document.getElementById("forceRecalc").checked;
    const processAll = document.getElementById("processAll").checked;

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

stopBtn.addEventListener("click", () => {
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

// Приём обновлений из content.js
chrome.runtime.onMessage.addListener((msg) => {
    if (msg?.target !== "sidepanel") return;

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