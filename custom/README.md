## Custom

Used to add your own custom css into the theme.

**Warning:** It is entirely possible to cause UI breakages using this feature. Please disable any custom css before troubleshooting or submitting issues.

Edit `custom.css` with your own changes and install with the `--custom-css` argument.

This file should be edited while within the installer directory, NOT after you've installed it to Steam. The latter will be overwritten on subsequent installs.

This is capable of overriding any of the current [css variables](/adwaita/css/_root):

```css
:root
{
	--adw-accent-bg-rgb: 53, 132, 228;
	--adw-accent-fg-rgb: 255, 255, 255;
	--adw-accent-rgb: 120, 174, 237;
}
```

For more advanced edits, you should reference [Inspecting Steam](https://github.com/tkashkin/Adwaita-for-Steam/tree/master/adwaita#inspecting-steam)