const scripts = [
    ["SP Desktop_", ["/adwaita/js/main/main.js"]],
    ["friendslist_", ["/adwaita/js/chat/chat.js"]],
    ["PopupWindow_", ["/adwaita/js/main/popup.js"]]
];

function inject(popup) {
    for (const [prefix, sources] of scripts) {
        if (!popup.m_strName.startsWith(prefix)) continue;
        for (const src of sources) {
            injectScript(popup.m_popup.document, src)
        }
        return;
    }
}

function injectScript(doc, src) {
    if ([...doc.scripts].some(s => s.src === src)) return;
    doc.head.append(Object.assign(doc.createElement("script"), { type: "module", src }));
}

g_PopupManager.GetPopups().forEach(inject);
g_PopupManager.AddPopupCreatedCallback(inject);