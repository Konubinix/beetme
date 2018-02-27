ASSETS = $(shell find assets/ -type f)

all: deploy

./node_modules/.bin/bower:
	npm install bower

json_deps: bower.json ./node_modules/.bin/bower
	./node_modules/.bin/bower install
	touch $@

venv:
	python3 -m venv venv
	./venv/bin/pip install -U wheel

python_deps: requirements.txt venv
	./venv/bin/pip install -U -r requirements.txt
	touch $@

beetme.html: beetme.py $(ASSETS) json_deps venv python_deps
	./venv/bin/python main.py build

dev: beetme.py $(ASSETS) json_deps python_deps venv python_deps
	./venv/bin/python main.py

deploy: beetme.html beetme.js beetme.png beetme.json
	rsync -avz $? beetmeserver:public_html
	touch $@
