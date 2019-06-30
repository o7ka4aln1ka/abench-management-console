#!/bin/sh

cd ~/github/abench-management-console/submodules/a-bench/ &&
echo "Start deploying the infrastructure!" 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
./admin.sh senv_a  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
sleep 15
mini_ip=$(minikube ip)
linkToDashboard="http://$(minikube ip):30002/dashboard/db/pods?orgId=1&var-namespace=kube-system&var-podname=etcd-minikube&from=now-15m&to=now&refresh=10s"
# opens some dash-boards
xdg-open $linkToDashboard &
minikube dashboard &
echo The infrastructure was deployed successfully! 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&

cd ~/github/abench-management-console/submodules/a-bench/ &&
./admin.sh down_submodules 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt &&
echo The BigBenchV2 submodule was successfully downloaded!  2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
