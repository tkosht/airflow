#!/usr/bin/sh

dag=$1
docker compose exec airflow-worker airflow dags trigger $dag
