#!/bin/sh

(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5

#install from FutureApp/a-bench
cd ~github/ &&
mkdir futureapp &&
cd futureapp/ &&
git clone https://github.com/FutureApp/a-bench.git &&
cd a-bench/ &&

wget https://raw.githubusercontent.com/FutureApp/a-bench/master/system_test/abench_prim_mods/test_install_on_new_machine.sh &&\
sudo bash test_install_on_new_machine.sh &&

sudo ./admin.sh auto_install &&

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
