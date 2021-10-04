migrate:
	docker-compose exec backend alembic upgrade head

migration:
	docker-compose exec backend alembic revision --autogenerate -m "$(message)"
	docker-compose exec backend alembic upgrade head

run_tests:
	docker-compose exec backend bash /app/tests-start.sh -x

run_tests_coverage:
	docker-compose exec backend bash /app/tests-start.sh --cov-report=html

dev:
	docker-compose up -d
	docker-compose logs -f backend

dev_build:
	docker-compose up -d --build
	docker-compose logs -f

down:
	docker-compose down

logs_backend:
	docker-compose logs -f backend

logs_proxy:
	docker-compose logs -f proxy

logs_frontend:
	docker-compose logs -f frontend
