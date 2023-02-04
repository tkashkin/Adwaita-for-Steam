#!/bin/bash
SKINS_DIR="../colorthemes"
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
	local sub_dir="$1"
	local fname="$2"
	local scale_down="${3:-0}"

	local args=()
	args+=("$SOURCE_DIR/$sub_dir/$fname.tga")
	args+=(-alpha "deactivate")
	args+=(-colorspace "gray")
	args+=(-sigmoidal-contrast "10,80%")
	args+=(+level-colors "$ACCENT,white")
	args+=(-alpha "activate")

	if [[ "$scale_down" -eq 1 ]]; then
		fname="${fname%@*}"
		args+=(-resize "50%")
	fi

	args+=("$out_sub_dir/$fname.tga")
	magick "${args[@]}"
}

function accent_shift_both_sizes() {
	accent_shift "$@"
	accent_shift "$@" 1
}

function mask_fill() {
	local sub_dir="$1"
	local fname="$2"
	local color="$3"
	local scale_down="${4:-0}"

	local args=()
	args+=("$SOURCE_DIR/$sub_dir/$fname.tga")
	args+=(-fill "$color")
	args+=(-colorize "100%")

	if [[ "$scale_down" -eq 1 ]]; then
		fname="${fname%@*}"
		args+=(-resize "50%")
	fi

	args+=("$out_sub_dir/$fname.tga")
	convert "${args[@]}"
}

function mask_fill_both_sizes() {
	mask_fill "$@"
	mask_fill "$@" 1
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
SCROLLBAR=$(get_color "scrollbar")

cecho p "Theme: $THEME"
cecho p "Accent: $ACCENT"
cecho p "Window BG: $WINDOW_BG"
cecho p "Headerbar BG: $HEADERBAR_BG"
cecho p "Headerbar Backdrop: $HEADERBAR_BACKDROP"
cecho p "Scrollbar BG: $SCROLLBAR"

mkdir -p "$OUT_DIR"

set_cur "avatar"
mask_fill_both_sizes "$sub_dir" "mask@2x" "$HEADERBAR_BG"
mask_fill_both_sizes "$sub_dir" "mask_backdrop@2x" "$HEADERBAR_BACKDROP"

set_cur "checkbox"
accent_shift_both_sizes "$sub_dir" "checked@2x"
accent_shift_both_sizes "$sub_dir" "checked_disabled@2x"
accent_shift_both_sizes "$sub_dir" "checked_hover@2x"

set_cur "checkbox_padded"
accent_shift_both_sizes "$sub_dir" "checked@2x"
accent_shift_both_sizes "$sub_dir" "checked_disabled@2x"
accent_shift_both_sizes "$sub_dir" "checked_hover@2x"

set_cur "corners/6_mask_window_bg"
mask_fill_both_sizes "$sub_dir" "bl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "br@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tr@2x" "$WINDOW_BG"

set_cur "corners/12_mask_window_bg"
mask_fill_both_sizes "$sub_dir" "bl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "br@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tr@2x" "$WINDOW_BG"

set_cur "corners/40_window_bg"
mask_fill_both_sizes "$sub_dir" "bl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "br@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tl@2x" "$WINDOW_BG"
mask_fill_both_sizes "$sub_dir" "tr@2x" "$WINDOW_BG"

set_cur "focusring/6"
accent_shift_both_sizes "$sub_dir" "bl@2x"
accent_shift_both_sizes "$sub_dir" "br@2x"
accent_shift_both_sizes "$sub_dir" "tl@2x"
accent_shift_both_sizes "$sub_dir" "tr@2x"

set_cur "focusring/12"
accent_shift_both_sizes "$sub_dir" "bl@2x"
accent_shift_both_sizes "$sub_dir" "br@2x"
accent_shift_both_sizes "$sub_dir" "tl@2x"
accent_shift_both_sizes "$sub_dir" "tr@2x"

set_cur "icons"
accent_shift_both_sizes "$sub_dir" "inbox_unread@2x"
accent_shift_both_sizes "$sub_dir" "inbox_unread_backdrop@2x"

set_cur "overlay"
mask_fill_both_sizes "$sub_dir" "close_bg@2x" "$HEADERBAR_BG"

set_cur "radiobutton"
accent_shift_both_sizes "$sub_dir" "checked@2x"
accent_shift_both_sizes "$sub_dir" "checked_disabled@2x"
accent_shift_both_sizes "$sub_dir" "checked_hover@2x"

set_cur "radiobutton_padded"
accent_shift_both_sizes "$sub_dir" "checked@2x"
accent_shift_both_sizes "$sub_dir" "checked_disabled@2x"
accent_shift_both_sizes "$sub_dir" "checked_hover@2x"

set_cur "scrollbar"
mask_fill_both_sizes "$sub_dir" "bottom@2x" "$SCROLLBAR"
mask_fill_both_sizes "$sub_dir" "bottom_active@2x" "$SCROLLBAR"
mask_fill_both_sizes "$sub_dir" "bottom_hover@2x" "$SCROLLBAR"
mask_fill_both_sizes "$sub_dir" "top@2x" "$SCROLLBAR"
mask_fill_both_sizes "$sub_dir" "top_active@2x" "$SCROLLBAR"
mask_fill_both_sizes "$sub_dir" "top_hover@2x" "$SCROLLBAR"

set_cur "switch"
accent_shift_both_sizes "$sub_dir" "checked@2x"
accent_shift_both_sizes "$sub_dir" "checked_disabled@2x"
accent_shift_both_sizes "$sub_dir" "checked_hover@2x"

cecho g "Done!"
