#!/bin/sh

(cd ~/github/a-bench-dashboard/submodules/a-bench/ &&
sudo ./admin.sh senv_a &&
sudo ./admin.sh down_submodules
) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
