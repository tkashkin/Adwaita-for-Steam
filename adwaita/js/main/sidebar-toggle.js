import { observeElements } from "../utils.js";

document.body.classList.add("adw-sidebar-toggle");

function setupSidebarToggle(id, sidebar, toggleParent = "&") {
    const toggleID = `adw-sidebar-toggle-${id}`;
    observeElements(sidebar, sidebar => {
        const _toggleParent = sidebar.querySelector(toggleParent);
        if (_toggleParent?.querySelector(`& > input.adw-sidebar-toggle`)) return;

        const toggle = Object.assign(document.createElement("input"), {
            type: "checkbox",
            id: toggleID,
            className: "adw-sidebar-toggle"
        });
        _toggleParent.prepend(toggle);

        const scrim = Object.assign(document.createElement("label"), {
            htmlFor: toggleID,
            className: "adw-sidebar-scrim"
        });
        sidebar.append(scrim);
    });
}

setupSidebarToggle("library-gamelist", "div._3x1HklzyDs4TEjACrRO2tB", "div._2TKEazUUS3TlniZfpc8OOe");