#!/bin/sh

# run an experiment with selected queries
(
. ~/github/abench-management-console/scripts/env_q29.txt
echo Selected queires were setted up as ENV VAR &&
cd ~/github/abench-management-console/submodules/a-bench/ &&
echo Starting Experiment: &&
./admin.sh run_sample_sre_bbv
echo The experiment was successfully executed! Find results under /submodules/a-bench/results/
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
