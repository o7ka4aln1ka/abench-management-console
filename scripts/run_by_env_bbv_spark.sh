#!/usr/bin/env bash

# run an experiment with selected queries (-- Uses the ENV- Experiments in [BBV2] for SPARk)
echo Selected queires were setted up as ENV VAR 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt &&
(
. ~/abench-management-console/scripts/env.txt
cd ~/wd/abench/a-bench/ &&
sudo ./admin.sh start_bbv_spark &&
echo Starting Spark Experiment:
TEST_QUERIES_TO_CALL=($TEST_QUERIES)
    if [ -z "$TEST_QUERIES_TO_CALL" ] ; then
        echo "Attention. No queries detected. Check the System-ENV > TEST_QUERIES"
    else
        echo "ENV-Looper-Experiment is starting now."
        for test_query in ${TEST_QUERIES_TO_CALL[@]}; do
            echo "Running $test_query"
            cd ~/wd/abench/a-bench/submodules/bigbenchv2/a-bench_connector/experiments/env-run-experiment/
            bash ENV_experiment_demoSPARK.sh run_ex  $test_query
        done
    fi
echo The Spark experiment was successfully executed! Find results under ~/wd/abench/a-bench/results/ &&
sudo chmod -R 777 ~/wd
) 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt
