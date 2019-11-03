#!/usr/bin/env bash

# -- Executes the SRE_experiment_demoHIVE.sh experiment in [BBV2]
# echo A sample single BigBenchV2 experiment will be executed: 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt &&
# (
cd ~/wd/abench/a-bench/ &&
sudo ./admin.sh start_bbv_hive
echo Starting Experiment: &&
./admin.sh run_sample_sre_bbv
# echo The experiment was successfully executed! Find results under ~/wd/abench/a-bench/results/ &&
sudo chmod -R 777 ~/wd
# ) 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt
