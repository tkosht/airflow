default: all

all: up

bash:
	docker compose exec airflow-webserver bash

# ==========
# docker compose aliases
up:
	docker compose up -d

ps images down:
	docker compose $@

im:images

build:
	docker compose build

build-no-cache:
	docker compose build --no-cache

reup: down up

clean: clean-logs clean-container clean-package

clean-logs:
	rm -rf logs/*

clean-container:
	docker compose down --rmi all

clean-package:
	rm -rf build *.egg-info
	find . -name '__pycache__' | xargs rm -rf

