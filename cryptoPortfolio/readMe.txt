portfolio.py:

This file is the actual cryptocurrency portfolio. To make it calculate your own profits and losses, modify the dictionary
called 'myPortfolio'. Change it so that it represents the type of coin you are holding, the amount, and how much was the unit
price when you bought it.

marketLooking.py:

This file retrieves the data from coinmarketcap.com every half an hour for the coins you declare and saves it in a csv file.
I do this to later use those files to build a correlation matrix.

correlationMatrix.py:

This file reads all the data files previously stored by marketLooking.py and then extracts the price of every coin in every file.
Afterwards, it build a correlation matrix. I did this in order to help me analyze if my portfolio was correctly diversified.