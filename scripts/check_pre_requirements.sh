#!/bin/bash

# Checks if a list of given programs are existing.
(function checkIfProgrammsExists() {
    echo "Checking if all required tools are available:"

    declare -a tools=("oracle-java8-set-default" "kubectl" "kubelet" "kubeadm" "minikube" "cat" "curl" "python3" "flask" "npm" "docker-ce" "nodejs" "python3-pip" "virtualbox")
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

echo "Systems will check the enviroment first, then it will install itself if all
requirements are full-filled."

checkIfProgrammsExists
) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
