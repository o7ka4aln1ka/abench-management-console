#!/bin/sh

# setup the environment 
(cd ~/github/abench-management-console/submodules/a-bench &&
sudo ./admin.sh auto_install
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
