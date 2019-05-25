#!/bin/sh

(
cd ~/github/a-bench-dashboard/submodules/a-bench/results && sudo chmod -R 777 . &&
echo Changed zip file to be reachable for all users &&
cd "$(dirname "$(find . -name 'experiment#01.zip*')")" &&
sleep 5
mkdir experiment_results &&
unzip 'experiment#01.zip' -d experiment_results &&
chmod -R 777 experiment_results
echo Created folder experiment_results

) 2>&1 | tee -a ~/github/a-bench-dashboard/output-homepage.txt
