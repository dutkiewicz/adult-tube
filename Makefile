format:
	black .
	isort --profile black .
	mypy --package extractor
	mypy --package web
