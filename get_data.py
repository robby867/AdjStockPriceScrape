#!python
# -*- coding: utf-8 -*-

"""Module to get adjusted close price from yahoo
   finance. Writes data to excel workbook with 
   tickers separated by worksheet
"""

import pandas_datareader as web
import xlsxwriter
import csv

__author__ = "Rob Yale"
__version__ = "1.0"
__status__ = "Prototype"

class GetData(object):
    
    # Returns a list of tickers from csv file specified
    def getTickers(self, file):
        tickers = []
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            
            # Skip over header
            next(reader)
            
            # Make list of tickers
            for row in reader:
                tickers.append(row[0])
                
        return tickers
    
    # Creates a workbook of adjusted close prices
    def createWorkbook(self):
        # Create workbook
        workbook = xlsxwriter.Workbook(self.file)
        
        # Add bold and date formats
        bold = workbook.add_format({'bold': 1})
        date_format = workbook.add_format({'num_format': 'mm/dd/yyyy'})
        
        # Loop over tickers
        error_tickers = []
        for ticker in self.tickers:
            print("writing ticker", ticker)
            
            # Try to get financial data for ticker symbol
            try:
                df = web.DataReader(ticker, data_source='yahoo', 
                                    start=self.start, end=self.end)
            except:
                # Continue to next ticker if failed
                print("could not get data for", ticker)
                error_tickers.append(ticker)
                continue
            
            # Start worksheet for ticker
            worksheet = workbook.add_worksheet(ticker)
            
            # Write header
            worksheet.write('A1', 'Date', bold)
            worksheet.write('B1', 'Adj Close', bold)
            
            # Format columns
            worksheet.set_column(0, 0, 10, date_format)
            worksheet.set_column(1, 1, 12)
            
            # Initialize rows
            xslxRow = 1
        
            # Write adj close data
            for index, row in df.iterrows():
                worksheet.write_datetime(xslxRow, 0, index, date_format)
                worksheet.write_number(xslxRow, 1, row["Adj Close"])
                xslxRow += 1
        
        # Close the workbook and save errors
        workbook.close()
        self.error_tickers = error_tickers
        print("Done")
                
    def __init__(self, start, end, csv, file):
        self.tickers = self.getTickers(csv)
        self.start = start
        self.end = end
        self.file = file
        self.error_tickers = None
        self.createWorkbook()

    def getErrors(self):
        return self.error_tickers














