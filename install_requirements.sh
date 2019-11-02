#!/bin/sh

(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5
sudo apt-get install -y python-pip -y &&
sleep 5
sudo apt-get install python3.6 -y &&
sleep 5
sudo pip install Flask -y &&
sleep 5
sudo pip install pandas &&
sleep 5
sudo apt-get install python3.6-tk -y &&
sleep 5
sudo apt-get install -y python3-pip python3-dev nginx &&
sleep 5
sudo add-apt-repository ppa:webupd8team/java &&
sudo apt update &&
sudo apt install -y oracle-java8-installer &&
# press enter to continue ??????
yes "" | command &&
sudo apt-get install oracle-java8-set-default -y &&
sleep 5
sudo apt-get install -y coreutils &&
sleep 5
sudo apt-get install curl &&
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
sudo  &&
echo All tools were installed! &&
sudo apt autoremove &&

# make all .py and .sh scripts executable
cd ~/github/abench-management-console/scripts -type f -iname "*.sh" -exec chmod +x {}
echo All .sh scripts were made executable
cd ~/github/abench-management-console/scripts -type f -iname "*.py" -exec chmod +x {}
echo All .py scripts were made executable

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
