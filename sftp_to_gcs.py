from airflow.providers.sftp.operators import sftp_operator
from airflow import DAG
import datetime

dag = DAG(
    'test_dag',
    start_date=datetime.datetime(2020, 1, 8, 0, 0, 0),
    schedule_interval='@daily'
)

put_operation = SFTPOperator(
    task_id="operation",
    ssh_conn_id="ssh_default",
    local_filepath="route_to_local_file",
    remote_filepath="remote_route_to_copy",
    operation="put",
    dag=dag
)
get_operation = SFTPOperator(....,
                             operation="get",
                             dag=dag
                             )

put_operation >> get_operation
