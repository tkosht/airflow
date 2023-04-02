from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from tasks import create_docker_task


with DAG(
    "job_general_runner",
    start_date=datetime(2023, 4, 1),
    catchup=False,
    tags=["app"],
) as dag:
    docker_task_train = create_docker_task(runner_text="sh bin/train_general.sh", task_id="train", container_name="experiment.app.airflow")
    docker_task_eval = create_docker_task(runner_text="sh bin/eval_general.sh", task_id="eval", container_name="experiment.app.airflow")

    # Empty operations
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # workflow
    start >> docker_task_train >> docker_task_eval >> end
