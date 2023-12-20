run:
	python -m uvicorn src.__main__:app --reload

docker-build:
	docker build --pull --rm -f "dockerfile" -t backendkdashboard:latest "." 

docker-compose:
	docker compose -f "dockercompose.yml" up -d --build

docker-tag:
	docker tag backendkdashboard:latest clementraoul/dockerhub:backendkdashboard