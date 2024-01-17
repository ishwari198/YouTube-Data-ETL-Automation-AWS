# YouTube Data Pipeline with Apache Airflow

## Overview
This data pipeline automates the extraction, transformation, and loading (ETL) of YouTube data using the Google API. It involves creating an EC2 instance and S3 buckets on AWS, orchestrated by Apache Airflow through a Directed Acyclic Graph (DAG) file.

## Purpose
Automate YouTube data extraction, transformation, and loading for data-driven insights. Utilize Apache Airflow for scalable workflow orchestration with components like EC2, S3, and the YouTube Data API.

## Tools
- **Apache Airflow:**
  - DAGs, Operators, S3Hook.
- **Amazon EC2:**
  - Execution environment.
- **Amazon S3:**
  - Storage for transformed data.
- **YouTube Data API:**
  - Programmatically access YouTube data.
  
  **Credentials:**
  - Username: admin
  - Password: [Your_Password_Here]

## Tasks
1. **Extract Data from YouTube using Google API:**
   Use a Python script with the Google API client library to extract data from the YouTube API.

2. **Create EC2 Instance and S3 Buckets:**
   Set up an AWS environment, including creating an EC2 instance and S3 buckets. Choose Ubuntu for the EC2 machine, allow HTTPS, and preferably select t2.medium for the Airflow server.

3. **Run DAG File Using Airflow Server:**
   Set up the Airflow pipeline by writing a Python script (`youtube_dag.py`) that instantiates the DAG, defines tasks, and sets dependencies.

## Additional Notes
1. Create a directory in your S3 bucket (e.g., `youtube_dag`) and update the `airflow.cfg` file with your directory name.
2. Copy and paste your `youtube_etl.py` and `youtube_dag.py` files using nano or vim.
3. When your Airflow server runs, it will create a DAG named `youtube_dag`.
4. Click on `youtube_dag` and run the DAG. Check for success or failure. If failed, inspect your Airflow log. In your S3 bucket, you can find the CSV file.

## Learning Areas
- Airflow basics (DAGs, Operators).
- YouTube Data API usage.
- ETL concepts and efficient workflows.
- AWS basics (EC2, S3).
- Data pipeline architecture.
- Monitoring, troubleshooting, and best practices.
