#!/usr/bin/env bash

# setup the environment
(
#test_install_on_new_machine form FutureApp/a-bench
echo The preparation of the environment starts. Depending on the internet connection it can take up to an hour. Be patient!
wget https://raw.githubusercontent.com/FutureApp/a-bench/master/system_test/abench_prim_mods/test_install_on_new_machine.sh &&\
sudo bash test_install_on_new_machine.sh &&
sudo chmod -R 777 ~/wd
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
