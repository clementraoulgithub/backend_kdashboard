run:
	python -m uvicorn src.__main__:app --reload

docker-build:
	docker build --pull --rm -f "dockerfile" -t backendkdashboard:latest "." --platform linux/amd64 -t ghcr.io/clementraoulastek/backendkdashboard:latest

docker-compose:
	docker compose -f "dockercompose.yml" up -d --build

docker-save:
	docker save backendkdashboard:latest kamasdashboard:latest | gzip > deploiment.tar.gz

docker-push:
	docker push ghcr.io/clementraoulastek/backendkdashboard:latest