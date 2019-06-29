#!/bin/sh

# run a sample experiment
(
cd ~/github/abench-management-console/submodules/a-bench/ &&
echo Starting Experiment: &&
# ./admin.sh run_sample_sre_bbv &&
# ./admin.sh senv_a
# sleep 15
# mini_ip=$(minikube ip)
# linkToDashboard="http://$(minikube ip):30002/dashboard/db/pods?orgId=1&var-namespace=kube-system&var-podname=etcd-minikube&from=now-15m&to=now&refresh=10s"
# # opens some dash-boards
# xdg-open $linkToDashboard &
# minikube dashboard &
#
# ./admin.sh down_submodules

export TEST_QUERIES="q29 q30"
export EX_TAG="experiment_tag_sample"

./admin.sh run_by_env_bbv


echo The experiment was successfully executed! Find results under /submodules/a-bench/results/

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
