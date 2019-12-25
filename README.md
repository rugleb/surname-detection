[![Build Status](https://travis-ci.com/rugleb/surname-detection.svg?branch=master)](https://travis-ci.com/rugleb/surname-detection)
[![codecov](https://codecov.io/gh/rugleb/surname-detection/branch/master/graph/badge.svg)](https://codecov.io/gh/rugleb/surname-detection)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rugleb/surname-detection/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8-green)](https://www.python.org/)

# About

The [Surname-Detection](https://github.com/rugleb/surname-detection) is an API on top of the ML model that allows you to determine whether a word is a surname or not.

The ML model is built on [catboost](https://github.com/catboost/catboost) CatBoostClassifier, and the API is based on the [aiohttp](https://github.com/aio-libs/aiohttp) framework.

Only Python >= 3.7 is supported.

## Installation

Via pip (i strongly recommend using a virtual env):

```shell script
make install
```

## Run server:

Run development server:

```shell script
python main.py
```

Help:

```shell script
python main.py -h
```

## Testing

Run unittests:

```shell script
make test
```

Run unittests with code coverage:
```shell script
make cov
```

# Docker

Build the image:

```shell script
make build
```

Push image to docker hub and heroku registry:

```shell script
make deploy
```

# License

This project is open-sourced software licensed under the [MIT license](https://github.com/rugleb/surname-detection/blob/master/LICENSE).
