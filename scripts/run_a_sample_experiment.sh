#!/bin/sh

# run an experiment with selected queries
(
# . ~/github/abench-management-console/scripts/env_q29.txt
echo A sample single BigBenchV2 experiment will be executed: &&
cd ~/wd/abench/a-bench/ &&
echo Starting Experiment: &&
./admin.sh run_sample_sre_bbv
echo The experiment was successfully executed! Find results under ~/wd/abench/a-bench/results/
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
