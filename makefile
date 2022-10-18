start:
	env
	make lab2

lab2:
	make runst folder=dna file=dna-app

lab1:
	make runst folder=d1_demos file=stockapp

runst:
	cd ${folder} && streamlit run ${file}.py

env:
	venv\Scripts\activate

install:
	pip install streamlit
	pip install yfinance

save:
	git add --all
	git commit -m "save progress"
	git push origin HEAD
