import os
import docker

from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount



with DAG(
    "job_docker",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    docker_task = DockerOperator(
        docker_url="tcp://docker-proxy:2375",
        image="experiment.app",
        mounts=[
            Mount(
                # source="/home/user_name/pj/experiment",
                source=os.environ["EXPERIMENT_DIR"],
                target="/home/dsuser/workspace",
                type="bind",
            ),
        ],
        working_dir="/home/dsuser/workspace/backend",
        command="bash -c 'PYTHONPATH=. python app/executable/train_topicmodel.py --n-limit=1024 --pipe-file=data/pipe_topic-test.gz'",
        # container_name=None,
        auto_remove=True,
        mount_tmp_dir=False,
        task_id="task_train",
        device_requests=[docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])],
    )

    # Empty operations
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # Create a simple workflow
    start >> docker_task >> end
