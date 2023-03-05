import docker

from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.docker.operators.docker import DockerOperator


with DAG(
    "gpu_test",
    schedule_interval="@daily",
    start_date=datetime(2023, 3, 1),
    catchup=False,
    tags=["test"],
) as dag:

    docker_task = DockerOperator(
        docker_url="tcp://docker-proxy:2375",
        command="/usr/bin/nvidia-smi",
        image="nvidia/cuda:11.8.0-devel-ubuntu22.04",
        auto_remove=True,
        mount_tmp_dir=False,
        task_id="gpu_docker_task",
        device_requests=[docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])],
    )

    # Empty operations
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # Create a simple workflow
    start >> docker_task >> end
