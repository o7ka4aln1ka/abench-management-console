#!/usr/bin/env bash

# show Grafana dashboard (script from FutureApp/a-bench by M.Czaja)
(
cd ~/wd/abench/a-bench/ &&
sudo ./admin.sh show_grafana_das
echo Grafana dashboards available at http://192.168.99.100:30002/dashboard/db/pods?orgId=1&var-namespace=kube-system&var-podname=etcd-minikube&from=now-15m&to=now&refresh=10s
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
