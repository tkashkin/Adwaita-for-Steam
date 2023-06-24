#!/bin/bash

###########
# GLOBALS #
###########
# CLASSES
declare -A classes=(
	["allcollections_Container"]=""
	["appdetails_Container"]=""
	["apppartnereventspage_AppPartnerEventsBody"]=""
	["bottombar_BottomBarContainer"]=""
	["collectionview_Container"]=""
	["desktoptoasts_DesktopToastContainer_"]=""
	["downloads_DownloadsPage"]=""
	["gamelistbar_Container"]=""
	["library_AppDetailsMain"]=""
	["library_Container"]=""
	["login_Login_"]=""
	["steamdesktop_BrowserWrapper"]=""
	["steamdesktop_ContentFrame"]=""
	["steamdesktop_LocalContentContainer"]=""
	["steamdesktop_TopBar"]=""
	["steamdesktop_Wrapper"]=""
	["steamdesktopoverlay_Wrapper"]=""
)

DESKTOP_ID="\#SteamDesktop"
DESKTOP_CLASS="body\.DesktopUI"

# DIRS
SOURCE_DIR="../web/"

BASE_DIR="base"
EXTRAS_DIR="extras"
FULL_DIR="full"

STEAM="$HOME/.steam/steam"
STEAM_FLATPAK="$HOME/.var/app/com.valvesoftware.Steam/.steam/steam"

STEAM_CSS="$STEAM/steamui/css"
STEAM_CSS_FLATPAK="$STEAM_FLATPAK/steamui/css"

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

# ARRAY
declare -a sed_args=("-i")

#############
# FUNCTIONS #
#############
function cecho {
	local text

	# INDENT
	[[ "$3" == 1 ]] && local indent="  "

	case "$1" in
		b) text="${indent}${BLUE}${ARROW} ${2}${CEND}";;
		g) text="${indent}${GREEN}${CHECK} ${2}${CEND}";;
		p) text="${indent}${PURPLE}${INFO} ${2}${CEND}";;
		r) text="${indent}${RED}${CROSS} ${2}${CEND}";;
	esac

	echo -e "$text"
}

function fatal_error {
	cecho r "$1"
	exit
}

function set_sed_args {
	for i in "${!classes[@]}"; do
		if [[ -z "${classes[$i]}" ]]; then
			cecho p "$i: is empty. Skipping Replace..."
		else
			sed_args+=("-e"  "s/^\(\s\+\)\?\($DESKTOP_ID\|$DESKTOP_CLASS\)\(\s\+\)\(.${i}\)[A-Za-z0-9_-]\+/\1\2\3\4_${classes[$i]}/g")
		fi
	done
}

function run_sed {
	cecho b "Updating $1..."

	find "./$1" -type f -name "*.css" | while read file; do
		sed ${sed_args[@]} "$file"
	done
}

function set_classes_values {
	local class

	cecho b "Grabbing CSS classes from $CSS_DIR"

	for i in "${!classes[@]}"; do
		class=$(grep -hoPr -m 1 "(?<=${i}_)[0-9A-Za-z0-9_-]+" "$CSS_DIR" | head -n1)

		if [[ "$class" =~ [A-Za-z0-9_-]{5} ]]; then
			cecho b "$i: $class" 1
			classes[$i]="$class"
		else
			cecho p "${i}_${class} is invalid"
		fi
	done
}

function dep_check {
	ERROR=0

	# Check Script Dependencies
	declare script_deps=( find grep sed )
	for i in "${script_deps[@]}"; do
		if ! type -P "$i" > /dev/null; then
			cecho r "$i is missing from PATH."
			ERROR=1
		fi
	done

	if [[ "$ERROR" == 1 ]]; then
		fatal_error "Missing Script Dependencies"
	fi
}

##########
# SCRIPT #
##########
[[ ! -d "$SOURCE_DIR" ]] && fatal_error "web dir not found, make sure you are running this from inside the scripts folder."

if [[ -d "$STEAM_CSS_FLATPAK" ]]; then
	CSS_DIR="$STEAM_CSS_FLATPAK"
elif [[ -d "$STEAM_CSS" ]]; then
	CSS_DIR="$STEAM_CSS"
else
	CSS_DIR=""
fi

[[ -z "$CSS_DIR" ]] && fatal_error "Could not find steam's steamui/css folder."

cd "$SOURCE_DIR" || exit

dep_check
set_classes_values
set_sed_args

run_sed "$BASE_DIR"
run_sed "$FULL_DIR"
run_sed "$EXTRAS_DIR"
