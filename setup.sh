##JAVA
sudo apt update
sudo apt upgrade
sudo apt install apt-transport-https && sudo apt update && sudo apt install -y openjdk-8-jdk

##GRAKN
mkdir ./grakn
sudo apt install software-properties-common apt-transport-https
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 8F3DA4B5E9AEF44C
sudo add-apt-repository 'deb [ arch=all ] https://repo.grakn.ai/repository/apt/ trusty main'
sudo apt update
wget -r https://github.com/graknlabs/grakn/releases/download/1.5.9/grakn-core-all-linux-1.5.9.tar.gz
tar xzf ./github.com/graknlabs/grakn/releases/download/1.5.9/grakn-core-all-linux-1.5.9.tar.gz -C ./grakn/
rm -rI github.com

## NGROK
sudo apt install unzip
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ./ngrok-stable-linux-amd64.zip
rm ngrok-stable-linux-amd64.zip
./ngrok authtoken <YOUR_TOKEN>

##VENV
sudo apt-get install python3-pip
python3 -m pip install -U pip

##CONDA
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
sha256sum Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh
cd ~
source ~/.bashrc
cd ./course_chatbot

## SpaCy
conda install -c conda-forge spacy==2.2.0
python3 -m pip install "http://zil.ipipan.waw.pl/SpacyPL?action=AttachFile&do=get&target=pl_spacy_model_morfeusz-0.1.0.tar.gz"

## Morfeusz
wget -O - http://download.sgjp.pl/apt/sgjp.gpg.key|sudo apt-key add -
sudo apt-add-repository http://download.sgjp.pl/apt/ubuntu
sudo apt update

sudo apt install python3-morfeusz2
sudo apt install morfeusz2
python3 -m easy_install "http://download.sgjp.pl/morfeusz/20200308/Linux/18.04/64/morfeusz2-0.4.0-py3.6-Linux-amd64.egg"

##Requirements
python3 -m pip install -r requirements.txt

##GRAKN
sudo ./grakn/grakn-core-all-linux-1.5.9/grakn server start
sudo ./grakn/grakn-core-all-linux-1.5.9/grakn console --keyspace course --file ./knowledge_base/schema.gql
python3 ./knowledge_base/migrate.py
