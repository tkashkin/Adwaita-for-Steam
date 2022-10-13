#!/bin/sh
#rogi27

download()
{
    echo -e "\e[36mDownloading latest version...\e[0m"
    cd "$HOME"
    git clone https://github.com/tkashkin/Adwaita-for-Steam adwaita-steam
}

setup()
{
    echo -e "\e[32mRunning installation script...\e[0m"
    PYTHON=$(python3 --version)
    echo -e "Your Python version is\e[32m" $PYTHON "\e[0m"
    cd "$HOME/adwaita-steam"
    python3 install.py
}

cleanup()
{
    echo -e "Cleaning files..."
    rm -rf "$HOME/adwaita-steam"
}

if ! hash python3 2>/dev/null;
then
    echo -e "\n\e[31mYou don't have Python installed!\nDownload it from \e[33mhttps://www.python.org/\e[0m\n"
    exit
fi

download
setup
cleanup

echo -e "\n\e[32mAdwaita for Steam should be installed. \nBe sure to restart Steam!\e[0m\n"