#!/bin/sh

# cd ~/github/abench-management-console/submodules/a-bench/ &&
# echo "Start deploying the infrastructure!" 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
# ./admin.sh senv_a  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
# sleep 15
#
# echo The infrastructure was deployed successfully! 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
#
# cd ~/github/abench-management-console/submodules/a-bench/ &&
# ./admin.sh down_submodules 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
# echo The BigBenchV2 submodule was successfully downloaded!  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt


# setup the environment
(
# #test_install_on_new_machine form FutureApp/a-bench
wget https://raw.githubusercontent.com/FutureApp/a-bench/master/system_test/abench_prim_mods/test_install_on_new_machine.sh &&\
sudo bash test_install_on_new_machine.sh &&
sudo chmod -R 777 ~/wd
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
