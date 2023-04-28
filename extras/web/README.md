# Web Themes
These files provide overrides for web based elements in the steam client.

Each theme is split into sections and combined by `install.py` to produce the final theme.

`base` is a minimal theme providing only basic color changes.

`full` themes more heavily and attempts to cover more areas of the client.

`extras` are optional bits that may be added to the above themes.

# Configuring Colors

Edit `base/1_root.css`

# Inspecting Classes

You can use steam's built in chrome inspector to find classes by launching it with the `-dev` argument and hitting `F12`

(The Chat window will open two inspectors, only one is relevant)

Some classes will be randomly suffixed, eg `library_MainPanel_3BFcm`

You will need to use the `*=` selector for those:

```css
div[class*="library_MainPanel_"]
{
	background: purple !important;
}
```

To inspect JS created hover elements, the typical `F8` keybind to pause script execution doesn't seem to function.

However you may enter this snippet in the console and then hit `]` to achieve the same.

```javascript
document.addEventListener('keydown', function (e) {
  if (e.keyCode == 221) debugger;
}, { capture: true });
```
