#!/bin/sh

(cd ~/github/abench-management-console/submodules/a-bench &&
sudo ./admin.sh auto_install
# sudo ./admin.sh demo_from_scratch_env
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
