Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that allows users to select a stock, enter the quantity they want to track, calculate the total investment, display the stock details, and save the result to a text file.

Features
Supports the following stocks:
1.AAPL
2.TSLA
3.GOOGLE
4.MSFT
-Accepts stock names in uppercase or lowercase.
-Takes the required stock quantity as input.
-Calculates total investment using:
Total Investment = Stock Price × Quantity

-Displays:
Stock Name
Price
Quantity
Total Investment
-Saves the result in a result.txt file.
-Displays an error message for an invalid stock name.

Stock Prices Used
Stock  Price 
AAPL   180
TSLA   250
GOOGLE 150
MSFT   300
Note: These are sample prices defined in the program and are not live market prices.

Requirements
-Python 3.x
-No external libraries are required.

How to Run
1.Make sure Python is installed on your computer.
2.Save the program as stock_tracker.py.
3.Open a terminal or command prompt in the project folder.
4.Run:
python stock_tracker.py
5.Enter the stock name when prompted:
Enter Stock Name (AAPL/TSLA/GOOGLE/MSFT):
6.Enter the quantity:
Enter Quantity:
7.The program will display the stock details and save the result in result.txt.

Example
Input
Enter Stock Name (AAPL/TSLA/GOOGLE/MSFT): AAPL
Enter Quantity: 5
Output
------ STOCK DETAILS ------
Stock Name : AAPL
Price : 180
Quantity : 5
Total Investment : 900

Result saved in result.txt

Output File
After successful execution, the program creates a file named:
result.txt
The file contains information such as:
Stock Name : AAPL
Quantity : 5
Total Investment : 900

Project Structure
stock-tracker-python/
│
├── stock_tracker.py
├── result.txt
└── README.md
result.txt is generated automatically after a valid stock entry.

Error Handling
If the user enters a stock name that is not available in the program, it displays:
Invalid Stock Name!

Formula
Total Investment = Stock Price × Quantity
For example, if AAPL costs 180 and the quantity is 5:
180 × 5 = 900

Technologies Used
Python
Dictionaries
User Input
Conditional Statements
File Handling
Basic Arithmetic

Author
CodeAlpha Stock Tracker Project

SONAL SEN
