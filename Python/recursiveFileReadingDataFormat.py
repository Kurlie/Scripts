import glob
import os
from tkinter import W

# file directory variable where all text files are stored. File formats:
# {
#   "key":"value"
#   "key":"value"
#   "key":"value"
#   "key":"value"
#   "key":"value"
# }
errorDirectoryFiles = ".\errorFiles\*.txt"

# list variable storing each file as a row in the list
errorRows = []

# recursive brute force loop - building row from each file in directory
for filename in glob.glob(errorDirectoryFiles):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        text = f.read()
        text = text.replace('\n', '', -1).replace('{', '').lstrip().split(', ')
        errorRows.append(text)

column1 = ''
column2 = ''
column3 = ''
column4 = ''
column5 = ''

finalData = '{},{},{},{},{}\n'.format(
    column1, column2, column3, column4, column5)

# remove key from key value pair in each row
for i in errorRows:

    rowBuilder = ""

    for x in i:
        rowBuilder = rowBuilder + "," + x[x.find(':')+1:]
        if i.index(x) == len(i)-1:
            finalData = finalData + rowBuilder[1:]
    finalData = finalData + "\n"

# write final data set to file
errorList = open(".\listOfErrors.txt", "w")
errorList.write(finalData)
errorList.close()
