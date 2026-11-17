export function waitForElement(selector, parent = document.body) {
    const existing = parent.querySelector(selector);
    if (existing) return Promise.resolve(existing);
    return new Promise(resolve => {
        const observer = new MutationObserver(records => {
            for (const record of records) {
                for (const node of record.addedNodes) {
                    if (!(node instanceof Element)) continue;
                    const element = node.matches(selector) ? node : node.querySelector(selector);
                    if (!element) continue;
                    observer.disconnect();
                    resolve(element);
                    return;
                }
            }
        });
        observer.observe(parent, { childList: true, subtree: true });
    });
}

export function waitForChild(parent, selector) {
    const existing = [...parent.children].find(child => child.matches(selector));
    if (existing) return Promise.resolve(existing);
    return new Promise(resolve => {
        const observer = new MutationObserver(records => {
            for (const record of records) {
                for (const node of record.addedNodes) {
                    if (!(node instanceof Element) || !node.matches(selector)) continue;
                    observer.disconnect();
                    resolve(node);
                    return;
                }
            }
        });
        observer.observe(parent, { childList: true });
    });
}

export function observeElements(selector, callback, parent = document.body) {
    parent.querySelectorAll(selector).forEach(callback);
    const observer = new MutationObserver(records => {
        const added = new Set();
        for (const record of records) {
            for (const node of record.addedNodes) {
                if (node instanceof Element) added.add(node);
            }
        }
        for (const node of added) {
            let ancestor = node.parentElement;
            let nested = false;
            while (ancestor) {
                if (added.has(ancestor)) {
                    nested = true;
                    break;
                }
                ancestor = ancestor.parentElement;
            }
            if (nested) continue;
            if (node.matches(selector)) callback(node);
            node.querySelectorAll(selector).forEach(callback);
        }
    });
    observer.observe(parent, { childList: true, subtree: true });
    return observer;
}

export function observeChildren(parent, selector, callback) {
    for (const child of parent.children) {
        if (child.matches(selector)) callback(child);
    }
    const observer = new MutationObserver(records => {
        for (const record of records) {
            for (const node of record.addedNodes) {
                if (node instanceof Element && node.matches(selector)) {
                    callback(node);
                }
            }
        }
    });
    observer.observe(parent, { childList: true });
    return observer;
}