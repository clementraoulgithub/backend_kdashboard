[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)
![example workflow](https://github.com/clementraoulastek/backend_kdashboard/actions/workflows/dev-continuous-integration.yml/badge.svg)
![example workflow](https://github.com/clementraoulastek/backend_kdashboard/actions/workflows/publish-ghcr.yaml/badge.svg)

# Backend Kamas Dashboard

This repository aim to query all data from sqlite database.

# Conda env

A virtual environment is used to run the project. It is managed by conda.

## Create the environment

```bash
conda env create -f environment.yml
```

## Activate the environment

```bash
conda activate backend-kamas-dashboard
```

# Run the app 

## In dev mode
```bash
make run
```

## In prod mode

```bash
make run
```

# Run the tests

```bash
make test
```

# Deploy the app

## Build the docker image

```bash
make docker-build
```

## Push the docker image

```bash
make docker-push
```
