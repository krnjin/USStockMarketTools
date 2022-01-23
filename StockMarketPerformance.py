from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# input: should be an indicator to return stocks that are up/down
# ex) calculate_stock_perf(up) should return % of up(positive) stocks compared to prior day
def calculate_stock_perf(indicator):

	# url of slickcharts sp500
	url = "https://www.slickcharts.com/sp500"

	# parse the html
	response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(response).read()
	soup = BeautifulSoup(webpage, 'html.parser')
	
	# get the number of up/down
	counter_down = len(soup.find_all('img', {'src':'/img/down.gif'}))
	counter_up = len(soup.find_all('img',{'src':'/img/up.gif'}))

	# get the total count for tr elements
	#total_count = len(soup.find_all('tr'))

	# find all tr elements under the element tbody
	row = soup.find('tbody').find_all("tr")

	# get the length of the row list
	total_stock = len(row)
	
	# print total listed number of stock in sp500
	#print(total_stock)

	# count number of stocks that has down icon
	#print(counter)
	 
	# total number of tr elements
	# print(total_count) #-> 510
	
	# calculate counter/total stock and round it to 2 decimal points and convert
	# it to string
	res_down = str(round(((counter_down/total_stock)*100),2))
	res_up = str(round(((counter_up/total_stock)*100),2))

	if indicator=='up':
		return res_up
	else:
		return res_down

# test output
#print(calculate_stock_perf())



