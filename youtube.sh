sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas 
sudo pip install s3fs
sudo pip install google-api-python-client

#connect EC2 instance 
ssh -i "airflow1.pem" ubuntu@ec2-34-204-95-105.compute-1.amazonaws.com

#commands for install airflow on EC2
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install s3fs
sudo pip install pandas
sudo pip install google-api-python-client

#run the DAG
airflow standalone
