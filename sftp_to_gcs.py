from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow import DAG
import datetime

dag = DAG(
    'sftp_to_gcs_dag',
    start_date=datetime.datetime(2020, 1, 8, 0, 0, 0),
    schedule_interval='@daily'
)

get_operation = SFTPOperator(
    task_id="put_sftp",
    ssh_conn_id="ssh_default",
    local_filepath="/tmp/images",
    remote_filepath="/upload",
    operation="get",
    dag=dag
)
# get_operation = SFTPOperator(....,
#                              operation="get",
#                              dag=dag
#                              )

# put_operation >> get_operation
get_operation
