### overview of a data pipeline that extracts data from YouTube using the Google API, creates an EC2 instance and S3 buckets on AWS, and runs a Directed Acyclic Graph (DAG) file using an Airflow server.

Tasks <br>
1.Extract Data from YouTube using Google API: The first task involves using a Python script with the Google API client library to extract data from the YouTube API.<br/><br/>
2.Create EC2 Instance and S3 Buckets: The second task involves setting up an AWS environment. This includes creating an EC2 instance and S3 buckets.
It's recommended to select Ubuntu for the EC2 machine and allow HTTPS. If possible, select t2.medium to run the Airflow server as t2.micro can cause issues.<br/><br/>
3.Run DAG File Using Airflow Server: The final task involves setting up the Airflow pipeline. 
This includes writing a Python script named youtube_dag.py that instantiates the DAG, defines the tasks, and sets their dependencies.<br/><br/>

### Additiona Notes
1.Create a directory in your S3 bucket, for example, youtube_dag, and make sure to update the airflow.cfg file with your directory name.<br/>
2.Copy and paste your youtube_etl.py and youtube_dag.py files using nano or vim.<br/>
3.hen your Airflow server runs, it will create a DAG named youtube_dag.<br/>
4.Click on youtube_dag and run the DAG. It will show if it's successful or failed. if it's failed check yorur aiflow log.Now, in your S3 bucket, you can see the CSV file.<br/>

