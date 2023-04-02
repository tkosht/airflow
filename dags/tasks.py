import os
import docker

from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


def create_docker_task(runner_text: str, task_id: str, container_name: str):
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
        command=f"bash -c '{runner_text}'",
        container_name=container_name,
        auto_remove=True,
        mount_tmp_dir=False,
        task_id=task_id,
        device_requests=[docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])],
    )
    return docker_task


