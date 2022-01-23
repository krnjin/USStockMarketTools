from StockMarketPerformance import *
from IndividualStockPerformance import *

# Introduction
print("Please choose from the following:")
print("1. Calculate the total stock market performance and the volume")
print("2. Find information on individual tickers")

flag = "y"

while(flag == "y"):

	# Ask for selection (input) to choose from
	selection = input("\nEnter your selection: ")

	while(selection != "1" and selection != "2"):
		selection = input("\nWrong selection, please enter only number (enter 999 to Exit): ")
		if (selection == "999"):
			break

	if selection == "1":
		print("\nCalculating the performace of SP500 componenets...")
		print("% of stocks positive: "+calculate_stock_perf("up")+"%")
		print("% of stocks positive: "+calculate_stock_perf("down")+"%")
	elif selection == "2":
		stock_symbol = input("\nPlease enter the stock symbol you want to look up: ")
		individual_stock_performance(stock_symbol)	

	flag = input("\n\nDo you want to continue? (y/n) ")

	while(flag != "y" and flag != "n"):
		flag = input("\nWrong choice, please entry 'n' or 'y' only\n")


	
