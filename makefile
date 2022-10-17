start:
	streamlit run .\stockapp.py

install:
	pip install streamlit
	pip install yfinance

save:
	git add --all
	git commit -m "save progress"
	git push origin HEAD
