#!/bin/sh

(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5
sudo apt-get install -y kubelet kubeadm kubectl &&
sleep 5
sudo apt-get install virtualbox -y &&
sleep 5
sudo apt-get install docker-ce -y &&
sleep 5
sudo apt-get install python-pip -y &&
sleep 5
sudo apt-get install python3-pip -y &&
sleep 5
sudo apt-get install oracle-java8-set-default -y &&
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
sleep 5
sudo  &&
echo All tools were installed! &&
sudo apt autoremove &&

#  download FutureApp/a-bench repo for creating the infrastructure
echo FutureApp repository will be downloaded for future use ...
cd ~/github/abench-management-console && mkdir -p submodules && cd submodules && git clone https://github.com/FutureApp/a-bench.git &&
echo Submodule FutureApp was successfully downloaded!

# make all .py and .sh scripts executable
cd ~/github/abench-management-console/scripts -type f -iname "*.sh" -exec chmod +x {}
echo All .sh scripts were made executable
cd ~/github/abench-management-console/scripts -type f -iname "*.py" -exec chmod +x {}
echo All .py scripts were made executable

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
