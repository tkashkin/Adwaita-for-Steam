#!/bin/sh
#rogi27

download()
{
    printf "\e[36mDownloading latest version...\e[0m\n"
    cd "$HOME" || exit
    git clone https://github.com/tkashkin/Adwaita-for-Steam adwaita-steam
}

install()
{
    printf "\e[32mRunning installation script...\e[0m\n"
    PYTHON=$(python3 --version)
    printf "Using \e[32m%s\e[0m\n" "$PYTHON"
    cd "$HOME/adwaita-steam" || exit
    printf "\n\e[36mWhich theme type do you want to install?\e[0m\n"
    printf "\e[32m (1) base - Default variant. \e[0m\n"
    printf "\e[32m (2) full - Includes heavy theming of web elements. \e[0m\n"
    printf "\e[32m (3) none - Variant without web elements theming. \e[0m\n"
    printf "\n\e[36mEnter option number (from 1 to 3): \e[0m"
    while :
    do
        read -r USER_INPUT
        case $USER_INPUT in
            1)
                printf "\e[32mInstalling 'base' variant... \e[0m\n"
                python3 install.py -w base
                break
            ;;
            2)
                printf "\e[32mInstalling 'full' variant... \e[0m\n"
                python3 install.py -w full
                break
            ;;
            3)
                printf "\e[32mInstalling 'none' variant... \e[0m\n"
                python3 install.py -w none
                break
            ;;
            *)
                printf "\e[33mEnter option number (from 1 to 3): \e[0m"
            ;;
        esac
    done
}

cleanup()
{
    printf "Cleaning files...\n"
    rm -rf "$HOME/adwaita-steam"
}

if ! hash python3 2>/dev/null;
then
    printf "\n\e[31mYou don't have Python installed!\nDownload it from \e[33mhttps://www.python.org/\e[0m\n"
    exit
fi

download
install
cleanup

printf "\n\e[32mAdwaita for Steam should be installed. \nBe sure to restart Steam!\e[0m\n\n"