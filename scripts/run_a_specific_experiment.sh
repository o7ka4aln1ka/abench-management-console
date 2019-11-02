#!/bin/sh

# run an experiment with selected queries (script from FutureApp/a-bench by M.Czaja)
(
. ~/github/abench-management-console/scripts/env.txt
echo Selected queires were setted up as ENV VAR &&
# cd ~/github/abench-management-console/submodules/a-bench/ &&
cd ~/wd/abench/a-bench/ &&
echo Starting Experiment:
TEST_QUERIES_TO_CALL=($TEST_QUERIES)
    if [ -z "$TEST_QUERIES_TO_CALL" ] ; then
        echo "Attention. No queries detected. Check the System-ENV > TEST_QUERIES"
    else
        echo "ENV-Looper-Experiment is starting now."
        for test_query in ${TEST_QUERIES_TO_CALL[@]}; do
            echo "Running $test_query"
            cd submodules/bigbenchv2/a-bench_connector/experiments/env-run-experiment/
            bash ENV_experiment_demoHIVE.sh run_ex  $test_query
        done
    fi
echo The experiment was successfully executed! Find results under ~/wd/abench/a-bench/results/
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
