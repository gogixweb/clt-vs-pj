install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

run:
	python manage.py runserver

build:
	cd frontend && npm run build 

server:
	cd frontend && npm run serve