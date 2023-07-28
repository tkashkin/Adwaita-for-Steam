# Theme
These files provide overrides for elements in the steam client.

The theme is split into sections and imported by `steamui/libraryroot.custom.css` to produce the final theme.

# Inspecting Steam

## Remote Debugging

To remotely inspect steam with a chromium browser:

1. Ensure nothing is running on your machine that uses port `8080` (Syncthing, etc)
2. Launch steam with the `-cef-enable-debugging` argument e.g. `steam -cef-enable-debugging`
3. Visit `chrome://inspect/#devices` in your Chromium based browser
4. Under `Discover network targets`, make sure `localhost:8080` is present
5. Steam entries should start showing up

This method has several benefits over the below method, allowing you to inspect Steam's In-Game Overlay and other hidden menus.

## Dev Mode

While more limited than the above, you can use steam's built in chrome inspector to find classes.

1. Launch steam with the `-dev` argument e.g. `steam -dev`
2. Press `F12` or Right Click -> inspect element

(Some windows may open two inspectors, only one is relevant)

### Hover Elements

To inspect JS created hover elements, the typical `F8` keybind to pause script execution doesn't seem to function.

However you may enter this snippet in the console and then hit `]` to achieve the same.

```javascript
document.addEventListener('keydown', function (e) {
        if (e.keyCode == 221) debugger;
        }, { capture: true });
```

# Writing CSS rules

Some classes will be randomly suffixed, eg `library_MainPanel_3BFcm`

You will need to use the `*=` selector for these:

```css
div[class*="library_MainPanel_"]
{
	background: purple !important;
}
```
