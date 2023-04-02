from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from tasks import create_docker_task


with DAG(
    "job_tensorboard",
    start_date=datetime(2023, 4, 1),
    catchup=False,
    tags=["app"],
) as dag:
    docker_task_tensorboard = create_docker_task(runner_text="make tensorboard", task_id="tensorboard", container_name="experiment.app.airflow.tensorboard")

    # Empty operations
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # workflow
    start >> docker_task_tensorboard >> end
