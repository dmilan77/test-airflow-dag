from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow.contrib.operators.sftp_operator import SFTPOperation
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator

from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.utils.dates import days_ago


import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(2)

}

dag = DAG(
    'sftp_to_gcs_dag',
    default_args=default_args,
    start_date=datetime.datetime(2020, 1, 8, 0, 0, 0),
    schedule_interval='@daily'
)

get_operation = SFTPOperator(
    task_id="get_operation",
    ssh_hook=SSHHook("my_ssh_conn"),
    local_filepath="/tmp/dlp-test",
    remote_filepath="/home/ec2-user/dlp-test.csv",
    operation=SFTPOperation.GET,
    dag=dag
)

put_operation = FileToGoogleCloudStorageOperator(
    task_id="put_operation",
    src="/tmp/dlp-test",
    dst="dlp-test",
    bucket="dlp-testing-target",
    google_cloud_storage_conn_id="my-gcp-conn",
    dag=dag
)

get_operation >> put_operation
