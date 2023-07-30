# Color Themes

These files provide color themes for the installer. All themes are their dark variants.

## Format

### RGB Variables

Colors with a `_rgb` in their name require a special format: `R, G, B`.

Do not use hex notation `#RRGGBB` or `rgb()` functions with these.

Good:
```css
--var_rgb: 255, 255, 255;
```

Avoid:
```css
--var_rgb: rgb(255, 255, 255);
--var_rgb: #FFFFFF;
```

### Other Variables

Typical CSS notation is fine, but do not reference other css variables within a theme.

Good:
```css
--var: rgb(255, 255, 255);
--var: rgba(255, 255, 255);
--var: #FFFFFF;
```

Avoid:
```css
--var: var(--some-other-var);
```

## Variables

Themes can override any variable defined in [:root](/web/base/_root.css)

## Reference Theme

The `adwaita` theme is merely a reference file, it is not actually used by the installer.

It is more verbose than other themes for completion sake.

Typically you'll just want to base a new theme on one of the smaller themes.
