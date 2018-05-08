install:
      pip3 install -r requirements.txt

run:
      python3 -m server.py

lint:
      pep8 ./

test: lint
      pytest tests/
