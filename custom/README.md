## Custom

Used to add your own custom css into the theme.

**Warning:** It is entirely possible to cause UI breakages using this feature. Please disable any custom css before troubleshooting or submitting issues.

Edit `custom.css` with your own changes and install with the `-cu` argument.

This file should be edited while within the installer directory, NOT after you've installed it to Steam. The latter will be overwritten on subsequent installs.

This is capable of overriding any of the current [css variables](/adwaita/variants/base/_root.css):

```css
:root
{
	--bg: #FF0000;
	--fg: #000000;
}
```

For more advanced edits, you should reference [Inspecting Steam](https://github.com/tkashkin/Adwaita-for-Steam/tree/master/web#inspecting-steam)

