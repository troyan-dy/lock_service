setup:
	pip3.9 install -r requirements.txt
	pip3.9 install -r resuirements.dev.txt
test:
	python3.9 -m pytest tests/

lint:
	python3.9 -m mypy lock_service/
	python3.9 -m flake8 lock_service/ tests/

format:
	python3.9 -m black lock_service/ tests/
	python3.9 -m isort lock_service/ tests/
