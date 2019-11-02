#!/usr/bin/env bash

# show kubernetes dashboard (script from FutureApp/a-bench by M.Czaja)
(
cd ~/wd/abench/a-bench/ &&
sudo ./admin.sh show_kuber_das
echo Kubernetes dashboards available at http://127.0.0.1:46649/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy/
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
