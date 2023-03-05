from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# from app.component.ulid import build_ulid

# A DAG represents a workflow, a collection of tasks
# with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
with DAG(
    dag_id="demo", start_date=datetime(2023, 3, 1), schedule=None, tags=["test"]
) as dag:

    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        # print("airflow" + build_ulid(prefix="AFL"))
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
