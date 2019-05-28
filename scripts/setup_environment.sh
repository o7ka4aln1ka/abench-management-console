#!/bin/sh

(cd ~/github/a-bench-dashboard/submodules/a-bench/future-app/a-bench/ &&
sudo ./admin.sh auto_install
) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
