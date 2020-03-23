from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.utils.dates import days_ago


import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': days_ago(2)
     # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'sftp_to_gcs_dag',
    default_args=default_args,
    start_date=datetime.datetime(2020, 1, 8, 0, 0, 0),
    schedule_interval='@daily'
)

get_operation = SFTPOperator(
    task_id="put_sftp",
    ssh_hook=SSHHook(conn_id="my_ssh_conn"),
    local_filepath="/tmp/images",
    remote_filepath="/home/ec2-user",
    operation="get",
    dag=dag
)
# get_operation = SFTPOperator(....,
#                              operation="get",
#                              dag=dag
#                              )

# put_operation >> get_operation
get_operation
