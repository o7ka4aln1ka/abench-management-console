#!/bin/sh

(
cd ~/github/abench-management-console/submodules/a-bench/results && sudo chmod -R 777 . &&
echo Changed zip file to be editable for all users &&
cd "$(dirname "$(find . -name 'experiment_tag_sample_q*')")" &&
sleep 5
# mkdir ~/github/a-bench-dashboard/experiment_results_v2 &&
unzip -o '*.zip' -d ~/github/abench-management-console/experiment_results &&
chmod -R 777 experiment_results
echo Created folder experiment_results

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
