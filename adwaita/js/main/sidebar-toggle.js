import { observeElements } from "../utils.js";

document.body.classList.add("adw-sidebar-toggle");

function resolveParent(selector, self) {
    if (selector === "&") return self;
    if (!selector) return null;
    return document.querySelector(selector);
}

function setupSidebarToggle(id, sidebar, toggleParent = "&", scrimParent = "&") {
    const toggleID = `adw-sidebar-toggle-${id}`;
    const openClass = `adw-sidebar-${id}-open`;
    observeElements(sidebar, sidebar => {
        const _toggleParent = resolveParent(toggleParent, sidebar);
        const _scrimParent = resolveParent(scrimParent, sidebar);

        if (_toggleParent && !_toggleParent?.querySelector(":scope > input.adw-sidebar-toggle")) {
            const toggle = Object.assign(document.createElement("input"), {
                type: "checkbox",
                id: toggleID,
                className: "adw-sidebar-toggle"
            });
            toggle.addEventListener("change", () => {
                document.body.classList.toggle(openClass, toggle.checked);
            });
            _toggleParent.append(toggle);
        }

        if (_scrimParent && !_scrimParent?.querySelector(":scope > label.adw-sidebar-scrim")) {
            const scrim = Object.assign(document.createElement("label"), {
                htmlFor: toggleID,
                className: "adw-sidebar-scrim"
            });
            _scrimParent.append(scrim);
        }
    });
}

setupSidebarToggle("library-gamelist", "div._3x1HklzyDs4TEjACrRO2tB", "div._2TKEazUUS3TlniZfpc8OOe");
setupSidebarToggle("library-details", "div._2aor4XVOYzN1PBSREk0UbO", "div._1-9sir4j_KQiMqdkZjQN0u", null)