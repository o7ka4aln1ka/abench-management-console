#!/bin/sh

#  TODO add more tools
(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5
sudo apt-get install python-pip &&
sleep 5
sudo pip install flask -y &&
sleep 5
sudo apt-get install coreutils -y &&
sleep 5
sudo apt-get install curl -y &&
sleep 5
sudo apt-get install python3.6 -y &&
sleep 5
sudo apt-get install nodejs -y &&
sleep 5
sudo npm install chart.js --save -y &&

#  download FutureApp/a-bench repo for creating the infrastructure
echo FutureApp repository will be downloaded for future use ... 
cd ~/github/a-bench-dashboard && mkdir -p submodules && cd submodules && git clone https://github.com/FutureApp/a-bench.git

) 2>&1 | tee -a ~/github/a-bench-dashboard/output-homepage.txt
