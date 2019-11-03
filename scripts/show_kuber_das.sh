#!/usr/bin/env bash

# show kubernetes dashboard (script from FutureApp/a-bench by M.Czaja)
gnome-terminal -e 'bash -c "sudo minikube dashboard 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt"' # &&\
# exec sleep 10
