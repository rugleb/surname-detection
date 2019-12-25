[![Build Status](https://travis-ci.com/rugleb/surname-detection.svg?branch=master)](https://travis-ci.com/rugleb/surname-detection)
[![codecov](https://codecov.io/gh/rugleb/surname-detection/branch/master/graph/badge.svg)](https://codecov.io/gh/rugleb/surname-detection)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rugleb/surname-detection/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8-green)](https://www.python.org/)

## About

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

## Endpoints

### Ping

Checking the health (activity) of the server.  
Try it on heroku: [link](https://surname-detection.herokuapp.com/ping).

Request:

```
GET /ping 
```

Response:

```json
{
    "status": true,
    "data": {},
    "message": "pong"
}
```

### Detect

Request to determine whether this word is a surname.  
Try it on heroku: [link]([heroku](https://surname-detection.herokuapp.com/detect?surname=Фельдман)).

Request:

```
GET /detect?surname=Фельдман
```

Response:

```json
{
    "status": true,
    "data": {
        "confidence": 0.4994302487
    },
    "message": "OK"
}
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

## Docker

Build the image:

```shell script
make build
```

Push image to the [Docker Hub](https://hub.docker.com/repository/docker/rugleb/surname-detection) and Heroku registry:

```shell script
make deploy
```

## License

This project is open-sourced software licensed under the [MIT license](https://github.com/rugleb/surname-detection/blob/master/LICENSE).
