#!/usr/bin/sh

dag=${1-job_demo}
docker compose exec airflow-worker airflow dags trigger $dag
