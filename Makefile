IMAGE_NANE=surname-detector

install:
	pip install --upgrade --no-cache-dir pip -r requirements-dev.txt

test:
	python -m unittest -qvb

cov:
	coverage run --source project -m unittest -qvb
	coverage report
	coverage html -d coverage/html
	coverage xml -o coverage/cobertura.xml
	coverage erase

isort:
	isort -rc project
	isort -rc tests
	isort -rc gunicorn.config.py
	isort -rc main.py

lint: isort test cov

build:
	docker build . -t $(IMAGE_NANE):latest -f dockerfile

deploy: build
	docker tag $(IMAGE_NANE):latest rugleb/$(IMAGE_NANE):latest
	docker tag $(IMAGE_NANE):latest registry.heroku.com/surname-detection/web
	docker push rugleb/$(IMAGE_NANE):latest
	docker push registry.heroku.com/surname-detection/web

release: deploy
	heroku container:release web --app="surname-detection"

all: install lint test cov build

.PHONY: install cov isort lint build all

.DEFAULT_GOAL := all
