#!/bin/sh

# run a sample experiment
(
cd ~/github/a-bench-dashboard/submodules/a-bench/ &&
echo Starting Single Run Experiment with Query 29 &&
./admin.sh run_sample_sre_bbv &&
echo The experiment was successfully executed!

) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
