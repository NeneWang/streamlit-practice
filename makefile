start:
	env
	make lab5p

lab5p:
	make runst folder=d2 file=sp500-personal

lab5:
	make runst folder=d2 file=sp500

lab4:
	make runst folder=d2 file=football_app

lab3:
	make runst folder=d2 file=basketball_app
	
lab2:
	make runst folder=d2 file=dna-app

lab1:
	make runst folder=d1_demos file=stockapp

runst:
	cd ${folder} && streamlit run ${file}.py

env:
	venv\Scripts\activate

install:
	pip install streamlit
	pip install yfinance

deploy-sample:
	

save:
	git add --all
	git commit -m "save progress"
	git push origin HEAD
