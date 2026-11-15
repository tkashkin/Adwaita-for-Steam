import config from "../../config.js";

document.body.classList.add("adw-injected");

if (config) {
    import("./sidebar-toggle.js");
}