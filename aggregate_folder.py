# folder aggregater

from tkinter import *
import os
import sys
import pandas as pd
from tkinter import filedialog
import numpy as np
from difflib import SequenceMatcher

####################################### GUI ####################################
#window = tk.Tk()
#frame1 = tk.Frame(window, )

format = "csv"
# ask user to select folder and to select file type
foldername = filedialog.askdirectory(initialdir = "~/18_input")

# ask user for filter, selection, aggregation

################################### process ####################################
# read in data
total = pd.DataFrame()
namelist = [] # contains all names of file of processed data
                  # which is later used to infer filename
for filename in os.listdir(foldername):
    if filename.endswith(format):
        filepath = foldername + os.path.sep + filename
        #print(foldername + os.path.sep +(filename))
        data = pd.read_csv(filepath)
        total = pd.concat([total,data], ignore_index = True)
        namelist.append(filename)
        #print(namelist)
# filter, select, aggregate


# write aggregated dataset
print(namelist)
for i in range(len(namelist)-1):
    for j in range(i+1,len(namelist)):
        match = SequenceMatcher(None, namelist[i],namelist[j]).find_longest_match(0,max(len(namelist[i]),len(namelist[j])))
        print(match)


destination_name = filedialog.asksaveasfiename("~/")
