docker-build:
	docker build --pull --rm -f "dockerfile" -t backendkdashboard:latest "." 

docker-compose:
	docker compose -f "dockercompose.yml" up -d --build

