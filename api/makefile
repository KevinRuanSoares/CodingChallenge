run:
	poetry run uvicorn --host 127.0.0.1 --port 8080 --reload --log-level debug --app-dir src main:app

style:
	poetry run isort src/ tests/
	poetry run black src/ tests/
	poetry run flake8 --max-line-length=120 src/ tests/
	poetry run flake8 *.md Makefile --select=W291
	poetry run mypy src/ --install-types --non-interactive --show-error-codes --explicit-package-bases
	poetry run pylint -d duplicate-code src/

test:
	poetry run pytest -s -l -vvv tests/ --cov=src/ --cov-fail-under=80 --cov-report=xml --cov-report=term:skip-covered
