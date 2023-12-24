run:
	python -m uvicorn src.__main__:app --reload

lint:
	python -m isort . --profile black
	python -m black .
	python -m pylint src

docker-build:
	docker build . --tag ghcr.io/clementraoulastek/backendkdashboard:latest --platform linux/amd64

docker-compose:
	docker-compose -f "dockercompose.yml" up -d --build

docker-push:
	docker push ghcr.io/clementraoulastek/backendkdashboard:latest