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

dev_build:
	docker-compose up -d --build
