from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def individual_stock_performance(stock):


	# url of slickcharts sp500
	url = "https://www.robinhood.com/stocks/" + stock

	# parse the html
	response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	# exit if invalid stock symbol is entered
	try:
		webpage = urlopen(response).read()
	except:
		print("Invalid Stock Symbol.")
		return 

	soup = BeautifulSoup(webpage, 'html.parser')
	
	# find about section in robinhood
	about = soup.find_all("span", {'class':'css-ws71f5'})[1].text

	# find market cap 
	market_cap = soup.find("span",{'id':'sdp-stats-market-cap-tooltip'}).text

	print("-"*10+"ABOUT"+"-"*10)
	print(about)
	print("-"*10+"MARKET CAP"+"-"*10)
	print(market_cap)