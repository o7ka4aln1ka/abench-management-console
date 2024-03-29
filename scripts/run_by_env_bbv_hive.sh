#!/usr/bin/env bash

# run an experiment with selected queries (script from FutureApp/a-bench by M.Czaja)
echo Selected queires were setted up as ENV VAR 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt &&
(
. ~/abench-management-console/scripts/env.txt
cd ~/wd/abench/a-bench/ &&
sudo ./admin.sh start_bbv_hive &&
echo Starting Hive Experiment:
TEST_QUERIES_TO_CALL=($TEST_QUERIES)
    if [ -z "$TEST_QUERIES_TO_CALL" ] ; then
        echo "Attention. No queries detected. Check the System-ENV > TEST_QUERIES"
    else
        echo "ENV-Looper-Experiment is starting now."
        for test_query in ${TEST_QUERIES_TO_CALL[@]}; do
            echo "Running $test_query"
            cd ~/wd/abench/a-bench/submodules/bigbenchv2/a-bench_connector/experiments/env-run-experiment/
            bash ENV_experiment_demoHIVE.sh run_ex  $test_query
        done
    fi
echo The Hive experiment was successfully executed! Find results under ~/wd/abench/a-bench/results/ &&
sudo chmod -R 777 ~/wd &&
cp -R -u -p ~/wd/abench/a-bench/results/ ~/abench-management-console/all_executed_exp/ &&
echo A backup of the results can be found under ~/abench-management-console/all_executed_exp
) 2>&1 | tee -a ~/abench-management-console/outputs/output-homepage.txt
