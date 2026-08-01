export const waitForElement = (selector, parent = document.body) =>
    new Promise(resolve => {
        const el = parent.querySelector(selector);
        if (el) return resolve(el);

        const observer = new MutationObserver(() => {
            const el = parent.querySelector(selector);
            if (!el) return;
            resolve(el);
            observer.disconnect();
        });

        observer.observe(parent, { subtree: true, childList: true });
    });

export function observeElements(selector, callback, parent = document.body) {
    parent.querySelectorAll(selector).forEach(callback);
    const observer = new MutationObserver(records => {
        for (const record of records) {
            for (const node of record.addedNodes) {
                if (!(node instanceof Element)) continue;

                if (node.matches(selector)) {
                    callback(node);
                }

                for (const child of node.querySelectorAll(selector)) {
                    callback(child);
                }
            }
        }
    });
    observer.observe(parent, { childList: true, subtree: true });
    return observer;
}