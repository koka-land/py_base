const lastSyncedStateByTab = new Map();

function isJournalUrl(url = "") {
    return url.startsWith("https://school.mos.ru/") &&
        (url.includes("/journal") || url.includes("/grade"));
}

function notifyTabContext(tab, force = false) {
    if (!tab?.id) return;

    const url = tab.url || "";
    const onJournal = isJournalUrl(url);
    const cacheKey = `${onJournal}:${url}`;

    if (!force && lastSyncedStateByTab.get(tab.id) === cacheKey) {
        return;
    }
    lastSyncedStateByTab.set(tab.id, cacheKey);

    chrome.runtime.sendMessage({
        target: "sidepanel",
        type: "context_changed",
        url,
        isJournal: onJournal
    }).catch(() => {});
}

chrome.runtime.onInstalled.addListener(() => {
    if (chrome.sidePanel?.setPanelBehavior) {
        chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(err => {
            console.error("[МЭШ Ассистент] Ошибка настройки Side Panel:", err);
        });
    }
});

chrome.tabs.onActivated.addListener(({ tabId }) => {
    chrome.tabs.get(tabId, (tab) => {
        if (!chrome.runtime.lastError && tab) {
            notifyTabContext(tab, true);
        }
    });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.url) {
        notifyTabContext({ ...tab, id: tabId, url: changeInfo.url }, false);
    }
});

chrome.tabs.onRemoved.addListener((tabId) => {
    lastSyncedStateByTab.delete(tabId);
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

    if (message?.action === "open_url" && message.url) {
        const targetUrl = message.url;
        chrome.tabs.query({}, (tabs) => {
            const existing = (tabs || []).find(t => (t.url || "").startsWith(targetUrl));
            if (existing?.id) {
                chrome.tabs.update(existing.id, { active: true });
                if (existing.windowId !== undefined) {
                    chrome.windows.update(existing.windowId, { focused: true }).catch(() => {});
                }
            } else {
                chrome.tabs.create({ url: targetUrl, active: true });
            }
            sendResponse?.({ ok: true });
        });
        return true;
    }

    if (message?.target === "content") {
        const isContextCheck = message.payload?.action === "check_context";

        chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
            const tab = tabs?.[0];
            if (!tab?.id || !tab.url?.includes("school.mos.ru")) {
                if (!isContextCheck) {
                    chrome.runtime.sendMessage({
                        target: "sidepanel",
                        type: "error",
                        title: "Нет активного журнала МЭШ",
                        summary: "Откройте страницу электронного журнала на school.mos.ru и повторите запуск."
                    }).catch(() => {});
                } else {
                    chrome.runtime.sendMessage({
                        target: "sidepanel",
                        type: "page_context",
                        isJournalPage: false,
                        isClassJournal: false,
                        className: ""
                    }).catch(() => {});
                }
                sendResponse?.({ ok: false });
                return;
            }

            try {
                await chrome.scripting.executeScript({
                    target: { tabId: tab.id },
                    files: ["content.js"]
                });

                chrome.tabs.sendMessage(tab.id, message.payload, (response) => {
                    if (chrome.runtime.lastError) {
                        if (isContextCheck) {
                            chrome.runtime.sendMessage({
                                target: "sidepanel",
                                type: "page_context",
                                isJournalPage: isJournalUrl(tab.url),
                                isClassJournal: false,
                                className: ""
                            }).catch(() => {});
                        }
                        sendResponse?.({ ok: false });
                        return;
                    }

                    if (isContextCheck && response) {
                        chrome.runtime.sendMessage({
                            target: "sidepanel",
                            type: "page_context",
                            ...response
                        }).catch(() => {});
                    }
                    sendResponse?.({ ok: true });
                });
            } catch (err) {
                if (!isContextCheck) {
                    chrome.runtime.sendMessage({
                        target: "sidepanel",
                        type: "error",
                        title: "Ошибка подключения к странице",
                        summary: err.message
                    }).catch(() => {});
                }
                sendResponse?.({ ok: false });
            }
        });
        return true;
    }

    if (message?.target === "sidepanel") {
        chrome.runtime.sendMessage(message).catch(() => {});
    }
});