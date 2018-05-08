install:
	pip3 install -r requirements.txt

run:
	python3 -m server.py

lint:
	pycodestyle --exclude='./ENV/*.*' ./

test: lint
	pytest tests/

