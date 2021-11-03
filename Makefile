include .env

flake:
	flake8 backend/app/app

migrate:
	docker-compose run --rm backend alembic upgrade head

migration:
	docker-compose run --rm backend alembic revision --autogenerate -m "$(message)"

run_tests:
	docker-compose run --rm backend bash /app/tests-start.sh -x

run_tests_coverage:
	docker-compose run --rm backend bash /app/tests-start.sh --cov-report=html

dev:
	docker-compose up -d
	docker-compose logs -f backend

build:
	docker-compose up -d --build
	docker-compose logs -f

down:
	docker-compose down

logs:
	docker-compose logs -f

logs_backend:
	docker-compose logs -f backend

logs_proxy:
	docker-compose logs -f proxy

logs_frontend:
	docker-compose logs -f frontend

psql:
	docker-compose run --rm db psql -h db -U postgres

psql_test:
	docker-compose run --rm test_db psql -h test_db -U postgres