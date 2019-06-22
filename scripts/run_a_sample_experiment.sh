#!/bin/sh

# run a sample experiment
(
cd ~/github/abench-management-console/submodules/a-bench/ &&
echo Starting Experiment: &&
# ./admin.sh run_sample_sre_bbv &&
./admin.sh demo_from_scratch_env &&
echo The experiment was successfully executed!

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
