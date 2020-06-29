setup:
	python3 -m venv ~/.udemy
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb
	
lint:
	black */*.py
	pylint --disable=R,C */*.py
	
all: install lint