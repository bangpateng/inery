#!/bin/bash
clear
echo "==================================================================="
echo -e "\e[92m"
echo  "   ____          ____       _                    ";
echo  "  | __ )  __ _  |  _ \ __ _| |_ ___ _ __   __ _  ";
echo  "  |  _ \ / _' | | |_) / _' | __/ _ \ '_ \ / _' | ";
echo  "  | |_) | (_| | |  __/ (_| | ||  __/ | | | (_| | ";
echo  "  |____/ \__, | |_|   \__,_|\__\___|_| |_|\__, | ";
echo  "         |___/                            |___/  ";
echo -e "\e[0m"
echo "===================================================================" 

echo -e '\e[36mGarapan :\e[39m' Inery Task 3
echo -e '\e[36mAuthor :\e[39m' Bang Pateng
echo -e '\e[36mTelegram Group :\e[39m' @bangpateng_group
echo -e '\e[36mTelegram Channel :\e[39m' @bangpateng_airdrop
echo -e '\e[36mYoutube :\e[39m' Bang Pateng
echo -e '\e[36mWebsite :\e[39m' www.bangpatengnode.site
echo "======================================="

sleep 2

echo -e "\e[1m\e[32m1. Updating packages... \e[0m" && sleep 1
# update
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y make bzip2 automake libbz2-dev libssl-dev doxygen graphviz libgmp3-dev \
autotools-dev libicu-dev python2.7 python2.7-dev python3 python3-dev \
autoconf libtool curl zlib1g-dev sudo ruby libusb-1.0-0-dev \
libcurl4-gnutls-dev pkg-config patch llvm-7-dev clang-7 vim-common jq libncurses5 git

echo -e "\e[1m\e[32m2. Clone Github... \e[0m" && sleep 1
# Clone Github
cd ~
git clone --recursive https://github.com/inery-blockchain/inery.cdt

echo -e "\e[1m\e[32m3. Set Path... \e[0m" && sleep 1
# Set Path
export PATH="$PATH:$HOME/inery.cdt/bin:$HOME/inery-node/inery/bin"

echo -e "\e[1m\e[32m4. Create Folder... \e[0m" && sleep 1
# Create Folder
mkdir -p $HOME/inrcrud

echo '=============== SETUP FINISHED ===================' && sleep 1
