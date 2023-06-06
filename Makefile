limpar:
	cls

pytest:
	pytest

docker:
	docker-compose run --service-ports -e --rm api bash -c "uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

alembic:
	docker-compose run --service-ports -e --rm api bash -c "alembic revision --autogenerate -m inicial"

docker_bash:
	docker-compose run --service-ports -e --rm api bash