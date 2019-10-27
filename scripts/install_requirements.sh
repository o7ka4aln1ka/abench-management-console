#!/bin/sh

(
sudo apt-get update &&
sleep 5
sudo apt-get upgrade -y &&
sleep 5
# scripts from FutureApp/a-bench
# # https://vitux.com/how-to-install-virtualbox-on-ubuntu/
# sudo add-apt-repository -y multiverse
# sudo apt-get update
# sudo apt-get -y install virtualbox virtualbox-qt virtualbox-dkms &&
# sleep 5
# # https://vitux.com/how-to-install-virtualbox-on-ubuntu/
# sudo add-apt-repository -y multiverse
# sudo apt-get update
# sudo apt-get -y install git &&
# sleep 5
# # Install Docker CE
# ## Set up the repository:
# ### Update the apt package index
# apt-get purge -y docker-ce; sudo rm -rf /var/lib/docker ## delete current docker-env
# apt-get update
# ### Install packages to allow apt to use a repository over HTTPS
# apt-get update && apt-get install apt-transport-https ca-certificates curl software-properties-common
# ### Add Dockers official GPG key
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
#
# ### Add docker apt repository.
# add-apt-repository \
# "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
# $(lsb_release -cs) \
# stable"
#
# ## Install docker ce.
# apt-get update && apt-get install docker-ce=18.06.0~ce~3-0~ubuntu
#
# # Setup daemon.
# cat > /etc/docker/daemon.json <<EOF
# {
#   "exec-opts": ["native.cgroupdriver=systemd"],
#   "log-driver": "json-file",
#   "log-opts": {
#     "max-size": "100m"
#   },
#   "storage-driver": "overlay2"
# }
# EOF
#
# mkdir -p /etc/systemd/system/docker.service.d
# # Restart docker.
# systemctl daemon-reload
# systemctl restart
# ##
# sudo groupadd docker
# sudo usermod -aG docker $USER &&
# sleep 5
# #install minikube
# curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.31.0/minikube-linux-amd64 && \
# chmod +x minikube && \
# sudo cp minikube /usr/local/bin/ && \
# rm minikube
# sleep 5
# #install helm
# curl -Lo helm.tar.gz https://storage.googleapis.com/kubernetes-helm/helm-v2.12.3-linux-amd64.tar.gz && \
# tar -zxvf helm.tar.gz && \
# sudo mv linux-amd64/helm /usr/local/bin/helm && \
# rm helm.tar.gz && \
# rm -rf linux-amd64 &&
# sleep 5
#
# #install k8n-bare
# # instructions from :https://www.mirantis.com/blog/how-install-kubernetes-kubeadm/
# sudo su
# swapoff -a
# nano /etc/fstab
#
# # comment line with tells something about swap!
# # like #UUID=d0200036-b211-4e6e-a194-ac2e51dfb27d none         swap sw
#
# nano /etc/ufw/sysctl.conf
# # REBOOT NOW
# sudo su
# apt-get install ebtables ethtool
#
# sudo su
# apt-get update
# apt-get install -y docker.io apt-transport-https curl
# systemctl enable docker && systemctl start docker
#
# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
# cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
# deb http://apt.kubernetes.io/ kubernetes-xenial main
# EOF

sleep 5
sudo apt-get install python3.6 -y &&
sleep 5
sudo apt-get install -y python3-pip python3-dev nginx &&
sleep 5
sudo add-apt-repository ppa:webupd8team/java &&
sudo apt update &&
sudo apt install -y oracle-java8-installer &&
sudo apt-get install oracle-java8-set-default -y &&
sleep 5
sudo pip install Flask &&
sleep 5
sudo apt-get install -y coreutils &&
sleep 5
sudo apt-get install curl &&
sleep 5
sudo apt-get update && \
sudo apt-get install cat &&
sleep 5
sudo apt-get install nodejs -y &&
sleep 5
sudo apt install npm &&
sleep 5
sudo npm install chart.js --save &&
sleep 5
sudo  &&
echo All tools were installed! &&
sudo apt autoremove &&

#  download FutureApp/a-bench repo for creating the infrastructure
echo FutureApp/a-bench repository will be downloaded for future use ...
cd ~/github/abench-management-console && mkdir -p submodules && cd submodules && git clone https://github.com/FutureApp/a-bench.git &&
echo Submodule FutureApp was successfully downloaded!

# make all .py and .sh scripts executable
cd ~/github/abench-management-console/scripts -type f -iname "*.sh" -exec chmod +x {}
echo All .sh scripts were made executable
cd ~/github/abench-management-console/scripts -type f -iname "*.py" -exec chmod +x {}
echo All .py scripts were made executable

) 2>&1 | tee -a ~/github/abench-management-console/outputs/output-homepage.txt
