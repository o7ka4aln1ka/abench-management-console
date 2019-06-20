#!/bin/sh

(cd ~/github/a-bench-dashboard/submodules/a-bench &&
sudo ./admin.sh auto_install
# sudo ./admin.sh demo_from_scratch_env
) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
