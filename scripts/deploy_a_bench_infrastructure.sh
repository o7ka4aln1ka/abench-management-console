#!/bin/sh

cd ~/github/abench-management-console/submodules/a-bench/ &&
echo "Start deploying the infrastructure!" 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
./admin.sh senv_a  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
sleep 15

echo The infrastructure was deployed successfully! 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&

cd ~/github/abench-management-console/submodules/a-bench/ &&
./admin.sh down_submodules 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
echo The BigBenchV2 submodule was successfully downloaded!  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
