from StockMarketPerformance import *

# Introduction
print("Please choose from the following:")
print("1. Calculate the total stock market performance and the volume")
print("2. Find information on individual tickers")

flag = "y"

while(flag == "y"):

	# Ask for selection (input) to choose from
	selection = input("\nEnter your selection: ")

	while(selection != "1" and selection != "2"):
		selection = input("Wrong selection, please enter only number (enter 999 to Exit): ")
		if (selection == "999"):
			break

	if selection == "1":
		print("Calculating the performace of SP500 componenets...")
		print("% of stocks positive: "+calculate_stock_perf("up")+"%")
		print("% of stocks positive: "+calculate_stock_perf("down")+"%")

	flag = input("\n\nDo you want to continue? (y/n) ")

	while(flag != "y" and flag != "n"):
		flag = input("Wront choice, please entry 'n' or 'y' only\n")


	#elif selection == "2":
