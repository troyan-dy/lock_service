setup:
	python3 -m pip install -r requirements.txt
	python3 -m pip install -r resuirements.dev.txt
test:
	python3 -m pytest tests/

lint:
	python3 -m mypy lock_service/
	python3 -m flake8 lock_service/ tests/

format:
	python3 -m black lock_service/ tests/
	python3 -m isort lock_service/ tests/

start:
	docker compose up -d --build  && docker compose logs -f
stop:
	docker compose down
