chrome.runtime.onInstalled.addListener(() => {
    if (chrome.sidePanel?.setPanelBehavior) {
        chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(err => {
            console.error("[МЭШ Ассистент] Ошибка настройки Side Panel:", err);
        });
    }
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message?.action === "reload_active_tab") {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            const tab = tabs?.[0];
            if (tab?.id) {
                chrome.tabs.reload(tab.id);
            }
            sendResponse?.({ ok: Boolean(tab?.id) });
        });
        return true;
    }

    if (message?.target === "content") {
        chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
            const tab = tabs?.[0];
            if (!tab?.id || !tab.url?.includes("school.mos.ru")) {
                chrome.runtime.sendMessage({
                    target: "sidepanel",
                    type: "error",
                    title: "Нет активного журнала МЭШ",
                    summary: "Откройте страницу электронного журнала на school.mos.ru и повторите запуск."
                }).catch(() => {});
                sendResponse?.({ ok: false });
                return;
            }

            try {
                await chrome.scripting.executeScript({
                    target: { tabId: tab.id },
                    files: ["content.js"]
                });
                chrome.tabs.sendMessage(tab.id, message.payload);
                sendResponse?.({ ok: true });
            } catch (err) {
                chrome.runtime.sendMessage({
                    target: "sidepanel",
                    type: "error",
                    title: "Ошибка подключения к странице",
                    summary: err.message
                }).catch(() => {});
                sendResponse?.({ ok: false });
            }
        });
        return true;
    }

    if (message?.target === "sidepanel") {
        chrome.runtime.sendMessage(message).catch(() => {});
    }
});