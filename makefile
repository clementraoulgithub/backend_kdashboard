run:
	python -m uvicorn src.__main__:app --reload

lint:
	python -m isort . --profile black
	python -m black .

docker-build:
	docker build --pull --rm -f "dockerfile" -t backendkdashboard:latest "." --platform linux/amd64 -t ghcr.io/clementraoulastek/backendkdashboard:latest

docker-compose:
	docker compose -f "dockercompose.yml" up -d --build

docker-push:
	docker push ghcr.io/clementraoulastek/backendkdashboard:latest