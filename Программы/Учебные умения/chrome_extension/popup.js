document.addEventListener('DOMContentLoaded', async () => {
  const interfaceDiv = document.getElementById('mainInterface');
  const warningDiv = document.getElementById('warningMessage');

  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Проверяем, что мы находимся в журнале МЭШ
  if (!tab || !tab.url || !tab.url.includes("school.mos.ru") || !tab.url.includes("journal")) {
    interfaceDiv.style.display = 'none';
    warningDiv.style.display = 'block';
    return;
  } else {
    interfaceDiv.style.display = 'block';
    warningDiv.style.display = 'none';
  }
});

document.getElementById('startBtn').addEventListener('click', async () => {
  const forceRecalc = document.getElementById('forceRecalc').checked;
  const processAll = document.getElementById('processAll').checked;
  const statusDiv = document.getElementById('status');

  statusDiv.textContent = "Запуск робота...";

  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab || !tab.url || !tab.url.includes("school.mos.ru")) {
    statusDiv.textContent = "Ошибка: Откройте вкладку school.mos.ru";
    return;
  }

  // 1. Сначала принудительно внедряем content.js на страницу
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ['content.js']
  }, () => {
    // Проверяем, не возникла ли системная ошибка инъекции
    if (chrome.runtime.lastError) {
      statusDiv.textContent = "Ошибка: обновите страницу журнала!";
      return;
    }

    statusDiv.textContent = "Робот работает. Не трогайте мышь...";

    // 2. Только после успешного внедрения отправляем команду
    setTimeout(() => {
      chrome.tabs.sendMessage(tab.id, {
          action: "start",
          forceRecalc: forceRecalc,
          processAll: processAll
      }, (response) => {
          // Гасим возможную ошибку, если порт не открылся мгновенно
          if (chrome.runtime.lastError) {
              // Игнорируем или выводим мягко
          }
      });
    }, 200);
  });
});

document.getElementById('stopBtn').addEventListener('click', async () => {
  const statusDiv = document.getElementById('status');
  statusDiv.textContent = "Останавливаю робота...";

  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab && tab.url && tab.url.includes("school.mos.ru")) {
    chrome.tabs.sendMessage(tab.id, { action: "stop" }, () => {
      if (chrome.runtime.lastError) { /* игнорируем, если контент-скрипт еще не жил */ }
    });
  }
});