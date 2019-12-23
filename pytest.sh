#!/usr/bin/env bash

SOURCE_DIR="project"
COVERAGE_DIR="coverage"

coverage run --source ${SOURCE_DIR} -m unittest -qv
coverage report
coverage html -d ${COVERAGE_DIR}/html
coverage xml -o ${COVERAGE_DIR}/cobertura.xml
coverage erase
