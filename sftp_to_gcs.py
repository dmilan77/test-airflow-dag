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
    local_filepath="/tmp/images",
    remote_filepath="/home/ec2-user/README.rst",
    operation=SFTPOperation.GET,
    dag=dag
)

put_operation = FileToGoogleCloudStorageOperator(
    task_id="put_operation",
    src="/tmp/images",
    dst="from-aws",
    bucket="us-east1-test-1-af1252e3-bucket",
    google_cloud_storage_conn_id="my-gcp-conn",
    dag=dag
)
# get_operation = SFTPOperator(....,
#                              operation="get",
#                              dag=dag
#                              )

# put_operation >> get_operation
get_operation >> put_operation
