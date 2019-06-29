#!/bin/sh

(cd ~/github/abench-management-console/submodules/a-bench/ &&

# sudo ./admin.sh demo_from_scratch_env
# &&
# echo The infrastructure was deployed successfully! Check the experiment results in submodules/a-bench/results

./admin.sh senv_a &&
echo The infrastructure was deployed successfully! &&
sleep 15
mini_ip=$(minikube ip)
linkToDashboard="http://$(minikube ip):30002/dashboard/db/pods?orgId=1&var-namespace=kube-system&var-podname=etcd-minikube&from=now-15m&to=now&refresh=10s"
# opens some dash-boards
xdg-open $linkToDashboard &
minikube dashboard &

./admin.sh down_submodules
echo The BigBenchV2 submodule was successfully downloaded!

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
