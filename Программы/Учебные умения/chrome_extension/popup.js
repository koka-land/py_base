document.getElementById("startBtn").addEventListener("click", async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.id) return;

    const mode = document.querySelector('input[name="mode"]:checked')?.value || "background";
    const forceRecalc = document.getElementById("forceRecalc").checked;
    const processAll = document.getElementById("processAll").checked;

    try {
        await chrome.scripting.executeScript({
            target: { tabId: tab.id },
            files: ["content.js"]
        });

        chrome.tabs.sendMessage(tab.id, {
            action: "start",
            mode,
            forceRecalc,
            processAll
        });

        window.close();
    } catch (err) {
        alert("Откройте страницу электронного журнала МЭШ (school.mos.ru).");
    }
});

document.getElementById("stopBtn").addEventListener("click", async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.id) return;

    chrome.tabs.sendMessage(tab.id, { action: "stop" });
});