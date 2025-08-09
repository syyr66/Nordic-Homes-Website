.PHONY: migrate collectstatic

migrate:
	docker compose run --rm app python manage.py migrate

collectstatic:
	docker compose run --rm app python manage.py collectstatic --noinput