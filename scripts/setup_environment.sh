#!/bin/sh

# setup the environment
(
cd ~/github/abench-management-console/submodules &&
# #test_install_on_new_machine form FutureApp/a-bench
wget https://raw.githubusercontent.com/FutureApp/a-bench/master/system_test/abench_prim_mods/test_install_on_new_machine.sh &&\
sudo bash test_install_on_new_machine.sh &&
sudo chmod -R 777 ~/wd
mv ~/wd/abench ~/github/abench-management-console/submodules
sudo chmod -R 777 submodules/
# sudo ./admin.sh auto_install
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
