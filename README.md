# AdjStockPriceScrape
## Installation and Use
To install the required dependancies, use the following command
```
pip install -r requirements.txt
```
Run main.py, and a GUI will pop up

Start date is the start of the date range (inclusive). If there isn't data going that far back, the earliest price date will be used

End date is the end of the date range (inclusive)

File name is the name of the excel workbook created

Ticker location is the path to the csv of the ticker names

Save to is the path that the program will output the data

Outputs a single excel wookbook, with tickers separated by worksheet. Dates will be in the first column, and adjusted close price in the second column. It will be saved in the specified file path.

An ExampleTickers.csv is included to try out the program.
## Background
A family member needed to get historical adjusted close prices for calculating returns on securities. Downloading the csv files by hand took too long, so they needed a way to quickly get data they could use for manipulation in excel. They needed this done within a day.
## This Project
I quickly put together a program to retrieve adjusted close prices from Yahoo! Finance using pandas datareader, and then wrote the data to an excel workbook. The program takes in a csv file path of the tickers needed, start and end dates, the output file name, and the output file path. The program uses tkinter for a GUI to specify the input parameters, and validates user input. These inputs get sent to pandas datareader, which returns a dataframe of the necessary data. This data is parsed, and then written to an excel workbook. The workbook separates each ticker by worksheet, with the dates in the first column and adjusted close prices in the second. 

This project was mostly an exercise in using pandas datareader, manipulating dataframes, and using tkinter as a GUI. It is relatively simple, as it needed to be put together within a day for the family member.
## Problems
We ran into getting problems with getting accurate data for computing returns. They needed the dividends to properly calculate returns for the securities, but many of the APIs looked into either did not have the dividends for mutual funds or cost money. We settled on Yahoo! Finance's adjusted close price, but there are concerns on the accuracy of the using this data in calculating returns.

Tkinter's GUI for python simply did not look great, and would take too much time making the GUI look nice. Styling for the GUI also created extra code that makes the program look verbose. 
## Future Versions
In future versions, I would replace the GUI with a simple html/CSS/JavaScript frontend. This would clean up the code considerably, and using bootstrap and other styling the GUI would look more modern. I would also research more into free APIs that would return dividend data so that the returns could be more accuractely calculated. Lastly, I would serparate the GetData class into more methods to make the code more concise/pythonic. I would also allow the user to specify where they get their data from, as panda's datareader has multiple data sources.
