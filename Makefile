PIP ?= pip
PYTHON ?= python

SOURCES = project examples gunicorn.config.py main.py setup.py
TESTS = tests

PROJECT_NAME = surname-detection
IMAGE_NANE = $(PROJECT_NAME)

install:
	$(PIP) install --upgrade --no-cache-dir pip -r requirements-dev.txt

test:
	$(PYTHON) -m unittest -qvb

cov:
	coverage run --source project -m unittest -qvb
	coverage report
	coverage html -d coverage/html
	coverage xml -o coverage/cobertura.xml
	coverage erase

isort:
	isort -rc $(SOURCES) $(TESTS)

mypy:
	mypy $(SOURCES)

pylint:
	pylint $(SOURCES)

lint: isort mypy pylint test

build:
	docker build . -t $(IMAGE_NANE):latest -f dockerfile

deploy: build
	docker tag $(IMAGE_NANE):latest rugleb/$(IMAGE_NANE):latest
	docker tag $(IMAGE_NANE):latest registry.heroku.com/$(PROJECT_NAME)/web
	docker push rugleb/$(IMAGE_NANE):latest
	docker push registry.heroku.com/$(PROJECT_NAME)/web

release: deploy
	heroku container:release web --app="$(PROJECT_NAME)"

all: install lint cov build

.PHONY: install test cov isort mypy pylint lint build all

.DEFAULT_GOAL := all
