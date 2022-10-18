start:
	make lab2

lab2:
	cd dna && streamlit run 

lab1:
	cd d1_demos && streamlit run .\stockapp.py

install:
	pip install streamlit
	pip install yfinance

save:
	git add --all
	git commit -m "save progress"
	git push origin HEAD
