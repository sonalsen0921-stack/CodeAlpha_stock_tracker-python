# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 300
}

stock_name = input("Enter Stock Name (AAPL/TSLA/GOOGLE/MSFT): ").upper()

if stock_name in stocks:
    quantity = int(input("Enter Quantity: "))

    total = stocks[stock_name] * quantity

    print("\n------ STOCK DETAILS ------")
    print("Stock Name :", stock_name)
    print("Price :", stocks[stock_name])
    print("Quantity :", quantity)
    print("Total Investment :", total)

    file = open("result.txt", "w")
    file.write("Stock Name : " + stock_name + "\n")
    file.write("Quantity : " + str(quantity) + "\n")
    file.write("Total Investment : " + str(total))
    file.close()

    print("\nResult saved in result.txt")

else:
    print("Invalid Stock Name!")