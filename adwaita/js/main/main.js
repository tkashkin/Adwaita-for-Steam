const configModule = await import("../../config.js").catch(error => {
    console.warn("Adwaita-for-Steam JS config unavailable: ", error);
    return null;
});
const config = configModule?.default ?? null;

document.body.classList.add("adw-injected");

import("./sidebar-toggle.js");