#!/bin/bash

function nuke() {
gnome-terminal --
minikube stop; minikube delete
docker stop $(docker ps -aq)
rm -r ~/.kube ~/.minikube
sudo rm /usr/local/bin/localkube /usr/local/bin/minikube
systemctl stop '*kubelet*.mount'
sudo rm -rf /etc/kubernetes/
docker system prune -af --volumes
}

function instal_kube-ctl() {
    sudo apt-get update && sudo apt-get install -y apt-transport-https
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
    sudo apt-get update
    sudo apt-get install -y kubectl
}


# Checks if a list of given programs are existing.
# Will print a summary and will stop the exection if
# a program of the list is not available or installed
function checkIfProgrammsExists() {
    echo "Checking if all required tools are available:"

    declare -a tools=("kubectl" "minikube" "cat")
    error_counter=0

    for tool in "${tools[@]}"
        do
            if ! [ -x "$(command -v ${tool})" ];
            then
                echo " [ ] [${tool}] is not installed." >&2
                error_counter=$[$error_counter +1]
            else
                echo " [x] [${tool}] is installed." >&2
            fi
        done

    if [ ! "$error_counter" == "0" ]; then
        echo ""
        echo "************************************************* ERROR **"
        echo "*                                                         "
        echo "* (${error_counter} of ${#tools[@]}) programs are missing."
        echo "* System detected some issues and will stop now.          "
        echo "* Please, fix the issues first then try again.            "
        echo "*                                                         "
        echo "**********************************************************"
        exit 1
    fi
}

# -----------------------------------------------------------------------[MAIN]--
curpath="$(pwd)"

temp='/home/vr/test/temp'

#-------------------------------------[ start ]-
echo "A-Bench for minikube-enviroment."
echo "Systems will check the enviroment first, then it will install itself if all
requirements are full-filled."

checkIfProgrammsExists

#-------------------------------------[ clean ]-
echo "System is cleaning... "
minikube stop; minikube delete
# TODO Write alternative procedure which checks before running
# optional -- system will hang if running without this ressources
# kubectl delete -n default deployment --all
# kubectl delete service spark-master
########
echo "System is now clean."


#-------------------------------------[ install ]-
minikube start
rm -rf $temp; mkdir -p $temp

# otherwise we will use the docker of the current host not
# the docker of minikube
eval $(minikube docker-env)

echo "System resouce-gather phase... "
cd $temp
git clone -b master https://github.com/FutureApp/kubernetes-spark.git
cd $temp/kubernetes-spark/docker
docker build -t spark-2.1.0-bin-hadoop2.6 .

echo "Resource creating phase ..."
wait_time=60
echo "sleeping now for $wait_time s" && sleep ${wait_time}
cd $temp/kubernetes-spark/
kubectl create -f spark-master.yaml           # creates th9 pod
kubectl create -f spark-master-service.yaml   # creates a kubectl-service
kubectl create -f spark-worker.yaml           # creates a worker-pod


## ex
sleep ${wait_time}
hostPortForSparkMaster=8090

echo "System-staging phase ..."
echo "sleeping now for $wait_time s"
sparkMasterName=$(kubectl get po | grep master* | awk '{print $1}')
echo found $sparkMasterName

# runs cmd in the background in the background
$(kubectl port-forward $sparkMasterName $hostPortForSparkMaster:8080) &

echo 'System is running now...'
echo "---------------------------------------------------- [Summary] --"
echo " minikube dashboard is available on $(minikube dashboard --url)                                                             "
echo " spark-master web-ui is listening on http://localhost:${hostPortForSparkMaster}"
echo "  "
