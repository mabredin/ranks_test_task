PACKAGE_MANAGER_RUNNER = conda run

runserver:
	$(PACKAGE_MANAGER_RUNNER) python manage.py runserver

makemigrations:
	$(PACKAGE_MANAGER_RUNNER) python manage.py makemigrations

migrate:
	$(PACKAGE_MANAGER_RUNNER) python manage.py migrate

shell:
	$(PACKAGE_MANAGER_RUNNER) python manage.py shell

lint:
	$(PACKAGE_MANAGER_RUNNER) black src
	$(PACKAGE_MANAGER_RUNNER) isort src

docker-up:
	docker compose up -d

docker-down:
	docker compose down -v