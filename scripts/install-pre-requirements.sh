#!/bin/sh

#  TODO add more tools

sudo apt-get update  # To get the latest package lists
sleep 5
sudo apt-get install FLask -y
sleep 5
sudo apt-get install cat -y
sleep 5
sudo apt-get install curl -y
sleep 5
sudo apt-get install python3.6 -y
sleep 5
sudo apt-get install nmp -y
sleep 5
sudo npm install chart.js --save -y

#  download FutureApp/a-bench repo for creating the infrastructure
cd ~/github/a-bench-dashboard && mkdir -p submodules && cd submodules && git clone https://github.com/FutureApp/a-bench.git 2>&1 | tee -a ~/github/a-bench-dashboard/test_output.txt
