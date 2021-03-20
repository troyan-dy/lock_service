setup:
	pip3.9 install -r requirements.txt
	pip3.9 install -r resuirements.dev.txt
test:
	pytest tests/
