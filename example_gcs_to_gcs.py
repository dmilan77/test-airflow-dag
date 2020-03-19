from airflow.operators.bash_operator import BashOperator

with models.DAG(
            dag_name,
            schedule_interval=timedelta(days=1),
            default_args=default_dag_args) as dag:

        copy_files = BashOperator(
            task_id='copy_files',
            bash_command='gsutil -m cp test1 test2'
        )
