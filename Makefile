prod:
	docker-compose -f docker-compose.yml up --build -d

dev:
	docker-compose -f docker-compose-dev.yml up --build

psql:
	docker-compose exec db psql -U postgres postgres

web:
	docker-compose exec web /bin/bash

db_revision:
	docker-compose exec web alembic revision --autogenerate

db_update:
	docker-compose exec web alembic upgrade head
