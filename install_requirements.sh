#!/usr/bin/env bash

(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5
sudo apt-get install python3 -y &&
sleep 5
sudo apt-get install -y python3-pip -y &&
sleep 5
sudo pip3 install Flask &&
sleep 5
# !!!!!! careful with pip and pip3 and python and python3
sudo pip3 install pandas &&
sleep 5
sudo apt-get install python3-tk -y &&
sleep 5
sudo add-apt-repository ppa:webupd8team/java &&
sudo apt-get install oracle-java8-set-default -y &&
sleep 5
sudo apt-get install -y coreutils &&
sleep 5
sudo apt-get install curl -y &&
sleep 5
sudo apt-get update && \
sudo apt-get install cat &&
sleep 5
sudo apt-get install nodejs -y &&
sleep 5
sudo apt install npm -y &&
sleep 5
sudo npm install chart.js --save &&
sleep 5
sudo apt update &&
sudo apt install openjdk-8-jre-headless -y &&
# sudo apt install oracle-java8-installer -y &&
sudo apt autoremove &&

# make all .py and .sh scripts executable
cd ~/abench-management-console/scripts -type f -iname "*.sh" -exec chmod +x {}
echo All .sh scripts were made executable
cd ~/abench-management-console/scripts -type f -iname "*.py" -exec chmod +x {}
echo All .py scripts were made executable

) 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt
