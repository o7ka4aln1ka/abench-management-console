#!/bin/sh

(
cd ~/github/a-bench-dashboard/submodules/a-bench/results && sudo chmod -R 777 . &&
echo Changed zip file to be editable for all users &&
cd "$(dirname "$(find . -name 'experiment#01.zip*')")" &&
sleep 5
# mkdir ~/github/a-bench-dashboard/experiment_results_v2 &&
unzip -o 'experiment#01.zip' -d ~/github/a-bench-dashboard/experiment_results_v2 &&
chmod -R 777 experiment_results
echo Created folder experiment_results

) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
 
