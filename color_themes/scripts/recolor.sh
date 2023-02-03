#!/bin/bash
SKINS_DIR=".."
SOURCE_DIR="../../Adwaita/assets"
OUT_DIR="recolored"

THEME="${1:-adwaita}"
THEME_FILE="$SKINS_DIR/$THEME/$THEME.theme"

# COLORS
BLUE="\e[34m"
GREEN="\e[32m"
PURPLE="\e[35m"
RED="\e[31m"
CEND="\e[0m"

# UNICODE ICONS
ARROW="→"
CHECK="✓"
CROSS="✖"
INFO="✦"

ORIG_ACCENT="#3584E4"
ACCURATE_ACCENT=0

function cecho {
	local text

	case "$1" in
		b) text="${BLUE}${ARROW} ${2}${CEND}";;
		g) text="${GREEN}${CHECK} ${2}${CEND}";;
		p) text="${PURPLE}${INFO} ${2}${CEND}";;
		r) text="${RED}${CROSS} ${2}${CEND}";;
	esac

	echo -e "$text"
}

function get_color() {
	grep -oP "(?<=$1 = )#[0-9a-fA-F]{6}" "$THEME_FILE"
}

function set_cur() {
	cecho b "$1"
	sub_dir="$1"
	out_sub_dir="$OUT_DIR/$sub_dir"
	mkdir -p "$out_sub_dir"
}

function accent_shift() {
	local fname="${1##*/}"
	if [[ "$ACCURATE_ACCENT" -eq 1 ]]; then
		./replacecolor -i "$ORIG_ACCENT" -o "$ACCENT" "$SOURCE_DIR/$1" "$out_sub_dir/$fname";
	else
		magick "$SOURCE_DIR/$1" -alpha deactivate -colorspace gray -auto-level +level-colors "$ACCENT",white -alpha activate "$out_sub_dir/$fname"
	fi
}

function mask_fill() {
	local fname="${1##*/}"
	local color="$2"
	convert "$SOURCE_DIR/$1" -fill "$color" -colorize 100% "$out_sub_dir/$fname";
}

### Start
if [[ ! -f "$THEME_FILE" ]]; then
	cecho r "$THEME_FILE not found"
	exit
fi

ACCENT=$(get_color "accent")
WINDOW_BG=$(get_color "window_bg")
HEADERBAR_BG=$(get_color "headerbar_bg")
HEADERBAR_BACKDROP=$(get_color "headerbar_backdrop")

cecho p "Theme: $THEME"
cecho p "Accent: $ACCENT"
cecho p "Window BG: $WINDOW_BG"
cecho p "Headerbar BG: $HEADERBAR_BG"
cecho p "Headerbar Backdrop: $HEADERBAR_BACKDROP"

if [[ ! -f "./replacecolor" ]]; then
	cecho p "---------"
	cecho p "replacecolor script not in current dir, using less accurate accent method"
	cecho p "replacecolor can be downloaded from: "
	cecho p "http://www.fmwconcepts.com/imagemagick/replacecolor/index.php"
else
	ACCURATE_ACCENT=1
fi

mkdir -p "$OUT_DIR"

set_cur "avatar"
mask_fill "$sub_dir/mask.tga" "$HEADERBAR_BG"
mask_fill "$sub_dir/mask@2x.tga" "$HEADERBAR_BG"
mask_fill "$sub_dir/mask_backdrop.tga" "$HEADERBAR_BACKDROP"
mask_fill "$sub_dir/mask_backdrop@2x.tga" "$HEADERBAR_BACKDROP"

set_cur "checkbox"
accent_shift "$sub_dir/checked.tga"
accent_shift "$sub_dir/checked@2x.tga"
accent_shift "$sub_dir/checked_disabled.tga"
accent_shift "$sub_dir/checked_disabled@2x.tga"
accent_shift "$sub_dir/checked_hover.tga"
accent_shift "$sub_dir/checked_hover@2x.tga"

set_cur "checkbox_padded"
accent_shift "$sub_dir/checked.tga"
accent_shift "$sub_dir/checked@2x.tga"
accent_shift "$sub_dir/checked_disabled.tga"
accent_shift "$sub_dir/checked_disabled@2x.tga"
accent_shift "$sub_dir/checked_hover.tga"
accent_shift "$sub_dir/checked_hover@2x.tga"

set_cur "corners/6_mask_window_bg"
mask_fill "$sub_dir/bl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/bl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr@2x.tga" "$WINDOW_BG"

set_cur "corners/12_mask_window_bg"
mask_fill "$sub_dir/bl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/bl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr@2x.tga" "$WINDOW_BG"

set_cur "corners/40_window_bg"
mask_fill "$sub_dir/bl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/bl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br.tga" "$WINDOW_BG"
mask_fill "$sub_dir/br@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tl@2x.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr.tga" "$WINDOW_BG"
mask_fill "$sub_dir/tr@2x.tga" "$WINDOW_BG"

set_cur "focusring/6"
accent_shift "$sub_dir/bl.tga"
accent_shift "$sub_dir/bl@2x.tga"
accent_shift "$sub_dir/br.tga"
accent_shift "$sub_dir/br@2x.tga"
accent_shift "$sub_dir/tl.tga"
accent_shift "$sub_dir/tl@2x.tga"
accent_shift "$sub_dir/tr.tga"
accent_shift "$sub_dir/tr@2x.tga"

set_cur "focusring/12"
accent_shift "$sub_dir/bl.tga"
accent_shift "$sub_dir/bl@2x.tga"
accent_shift "$sub_dir/br.tga"
accent_shift "$sub_dir/br@2x.tga"
accent_shift "$sub_dir/tl.tga"
accent_shift "$sub_dir/tl@2x.tga"
accent_shift "$sub_dir/tr.tga"
accent_shift "$sub_dir/tr@2x.tga"

set_cur "icons"
accent_shift "$sub_dir/inbox_unread.tga"
accent_shift "$sub_dir/inbox_unread@2x.tga"
accent_shift "$sub_dir/inbox_unread_backdrop.tga"
accent_shift "$sub_dir/inbox_unread_backdrop@2x.tga"

set_cur "overlay"
mask_fill "$sub_dir/close_bg.tga" "$HEADERBAR_BG"
mask_fill "$sub_dir/close_bg@2x.tga" "$HEADERBAR_BG"

set_cur "radiobutton"
accent_shift "$sub_dir/checked.tga"
accent_shift "$sub_dir/checked@2x.tga"
accent_shift "$sub_dir/checked_disabled.tga"
accent_shift "$sub_dir/checked_disabled@2x.tga"
accent_shift "$sub_dir/checked_hover.tga"
accent_shift "$sub_dir/checked_hover@2x.tga"

set_cur "radiobutton_padded"
accent_shift "$sub_dir/checked.tga"
accent_shift "$sub_dir/checked@2x.tga"
accent_shift "$sub_dir/checked_disabled.tga"
accent_shift "$sub_dir/checked_disabled@2x.tga"
accent_shift "$sub_dir/checked_hover.tga"
accent_shift "$sub_dir/checked_hover@2x.tga"

set_cur "scrollbar"
mask_fill "$sub_dir/bottom.tga" "$ACCENT"
mask_fill "$sub_dir/bottom@2x.tga" "$ACCENT"
mask_fill "$sub_dir/bottom_active.tga" "$ACCENT"
mask_fill "$sub_dir/bottom_active@2x.tga" "$ACCENT"
mask_fill "$sub_dir/bottom_hover.tga" "$ACCENT"
mask_fill "$sub_dir/bottom_hover@2x.tga" "$ACCENT"
mask_fill "$sub_dir/top.tga" "$ACCENT"
mask_fill "$sub_dir/top@2x.tga" "$ACCENT"
mask_fill "$sub_dir/top_active.tga" "$ACCENT"
mask_fill "$sub_dir/top_active@2x.tga" "$ACCENT"
mask_fill "$sub_dir/top_hover.tga" "$ACCENT"
mask_fill "$sub_dir/top_hover@2x.tga" "$ACCENT"

set_cur "switch"
accent_shift "$sub_dir/checked.tga"
accent_shift "$sub_dir/checked@2x.tga"
accent_shift "$sub_dir/checked_disabled.tga"
accent_shift "$sub_dir/checked_disabled@2x.tga"
accent_shift "$sub_dir/checked_hover.tga"
accent_shift "$sub_dir/checked_hover@2x.tga"

cecho g "Done!"
