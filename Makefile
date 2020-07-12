format:
	black .
	isort --recursive --profile black .
	mypy --package extractor
