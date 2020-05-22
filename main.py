#!python
# -*- coding: utf-8 -*-

"""GUI for get_data module. Validates user input, 
   and simplifies data retrieval
"""

import tkinter.filedialog
import tkinter as tk
import os
from datetime import datetime
from get_data import GetData

__author__ = "Rob Yale"
__version__ = "1.0"
__status__ = "Prototype"

# Set up GUI
root = tk.Tk()
root.geometry('500x380')
SPAN_WIDTH = 2
ENTRY_WIDTH = 23
FILE_WIDTH = 50
PADX = 10
PADY = (0, 10)

# Opens file browser
def browseFile(name):
    if(name == "csv"):
        filename = tk.filedialog.askopenfilename()
        if(len(filename) != 0):
            e4.delete(0,"end")
            e4.insert(0, filename)
    if(name == "save"):
        filename = tk.filedialog.askdirectory()
        if(len(filename) != 0):
            e5.delete(0,"end")
            e5.insert(0, filename)
        
# Validate date in mm/dd/yyyy format
def validDate(date):
    try:
        datetime.strptime(date, '%m/%d/%Y')
    except:
        return False
    else:
        return True

# Get stock data
def getData():
    # Get input text
    start = e1.get()
    end = e2.get()
    name = e3.get()
    csv = e4.get()
    file = e5.get()
    
    # Validate inputs
    if(not os.path.isfile(csv) and not csv.lower().endswith('.csv')):
        tk.messagebox.showerror("Error", "Invalid csv!", icon="error")
        return
    if(not validDate(start)):
        tk.messagebox.showerror("Error", "Invalid start date!", icon="error")
        return
    if(not validDate(end)):
        tk.messagebox.showerror("Error", "Invalid end date!", icon="error")
        return
    if(len(name) == 0):
        tk.messagebox.showerror("Error", "You need to name your file!", icon="error")
        return
    
    # Check if overwriting
    name = name + ".xlsx"
    if(not file.endswith("/")):
        file = file + "/"
        
    file = file + name
    if(os.path.exists(file)):
        question = name + " already exists. This will overwrite the file. Do you wish to continue?"
        msg = tk.messagebox.askquestion ("Overwrite", question, icon="warning")
        if(msg == "no"):
            return
        
    # Get data
    errors = []
    try:
        myData = GetData(start, end, csv, file)
        errors = myData.getErrors()
    except:
        tk.messagebox.showerror("Error", "Something went wrong", icon="error")
        return
    else:
        # Displays any errors getting tickers
        if(len(errors) != 0):
            msg = "The following ticker data could not be retrieved: " + " ".join(errors)
            tk.messagebox.showwarning('Error',msg, icon="warning")
        # Closes window if finished
        msg = tk.messagebox.askquestion('Finished','Do you want to get more data?')
        if(msg == "yes"):
            return
        else:
            root.destroy()


# Labels for input boxes
labels = ["Start Date (mm/dd/yyyy)", "End Date (mm/dd/yyyy)", "File Name", "Ticker Location (csv)"]
for i in range(len(labels)):
    tk.Label(root, text=labels[i]).grid(row=i*2, sticky="W")
tk.Label(root, text="Save to").grid(row=9, sticky="W")

# Entries
e1, e2, e3 = (tk.Entry(root, width=ENTRY_WIDTH), 
              tk.Entry(root, width=ENTRY_WIDTH), tk.Entry(root, width=ENTRY_WIDTH))
e4, e5 = tk.Entry(root, width=FILE_WIDTH), tk.Entry(root, width=FILE_WIDTH)
myEntries = [e1, e2, e3, e4, e5]

# Sets default values
today = datetime.today().strftime('%m/%d/%Y')
cwd = os.getcwd()
e1.insert(0, "12/31/1994")
e2.insert(0, today)
e3.insert(0, "Adj_Close_History")
#e4.insert(0, "")
e5.insert(0, cwd)

# Sets positioning
for e in range(4):
    myEntries[e].grid(row=(e*2)+1, sticky="W", pady=PADY)
e4.grid(columnspan = SPAN_WIDTH, pady = (0, 5))
e5.grid(row=10, columnspan = SPAN_WIDTH, sticky="W", pady=(0,5))

# Allows for span across multiple columns
for i in range(SPAN_WIDTH+1):
    root.grid_columnconfigure(i, weight=1, uniform="foo")
    
# Set up the browse buttons
btnBrowseCSV = tk.Button(root, height=1, width=10, text="Browse", 
                    command=lambda:browseFile("csv"))
btnBrowseSave = tk.Button(root, height=1, width=10, text="Browse", 
                    command=lambda:browseFile("save"))

btnBrowseCSV.grid(row=8, sticky="W", pady=(0,10))
btnBrowseSave.grid(row=11, sticky="W", pady=(0,10))

# Set up the get data button
btnGetData = tk.Button(root, height=2, width=20, text="Get Data", 
                    command=lambda:getData())
btnGetData.grid(row=12, sticky="W", pady=10)

for child in root.winfo_children():
    child.grid_configure(padx=10)

# Main loop
root.mainloop()