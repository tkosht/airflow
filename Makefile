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

clean: clean-logs clean-container

clean-logs:
	rm -rf log/*.log

clean-container:
	docker compose down --rmi all
	sudo rm -rf app/__pycache__
