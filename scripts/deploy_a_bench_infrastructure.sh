#!/bin/sh

(cd ~/github/a-bench-dashboard/submodules/a-bench/ &&
sudo ./admin.sh senv_a &&
echo The infrastructure was deployed successfully! &&
sudo ./admin.sh down_submodules
echo The BigBenchV2 submodule was successfully downloaded! 
) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
