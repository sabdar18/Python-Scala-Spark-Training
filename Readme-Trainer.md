## Install Docker
```
sudo apt -y update
sudo apt -y upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo apt-get update
sudo systemctl start docker
sudo systemctl enable docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/1.25.3/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
docker-compose --version
sudo usermod -aG docker $USER
exit
```

## Setup Shell in a Box (Access Ubuntu SSH/Shell/Console from Browser)
 - Refer: https://github.com/shellinabox/shellinabox
 - Refer: https://linoxide.com/web-remote-your-server/
```
sudo apt-get install openssl
sudo apt-get install shellinabox
sudo /etc/init.d/shellinabox start
sudo vi /etc/default/shellinabox
  - Modify to: SHELLINABOX_ARGS="--no-beep --disable-ssl"
sudo /etc/init.d/shellinabox restart
man shellinaboxd

```
 - Note: Use Ctrl+Shift+V to paste


## Setup Python and Jupyter Hub using Docker
```
docker pull atingupta2005/ubuntu_ml
docker run -it -p 8080:8080 -p 8000:8000 -p 81:81 -p 8888:8888 atingupta2005/ubuntu_ml /bin/bash
apt update
cd ~
source myvirtualenv/bin/activate
jupyterhub &
Visit http://pythonvm.westus.cloudapp.azure.com:8000/hub/login
Login using the user created on Unix - u1/p
```

# By Each Trainee
## Clone files
 - Open terminal from jupyter and run below commands
```
pwd
cd ~
pwd
git clone https://github.com/atingupta2005/Python-Scala-Spark-Training.git
```
