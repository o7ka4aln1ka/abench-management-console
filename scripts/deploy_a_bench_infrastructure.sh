#!/bin/sh

(cd ~/github/abench-management-console/submodules/a-bench/ &&

sudo ./admin.sh demo_from_scratch_env &&
echo The infrastructure was deployed successfully! Check the experiment results in submodules/a-bench/results

# sudo ./admin.sh senv_a &&
# echo The infrastructure was deployed successfully! &&
# sudo ./admin.sh down_submodules
# echo The BigBenchV2 submodule was successfully downloaded!
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
