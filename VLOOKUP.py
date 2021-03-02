#This script emulated the excel function VLOOKUP (value, table, col_index, [range_lookup])
#Follow the steps below to

import pandas as pandas
import numpy as np
import json

#step 1: copy and paste excel file path into parentheses on next line. include full file path
data = pandas.read_excel (r'C:\Users\epowl\Documents\Katvan Properties Llc\Contact Master list.xlsx')
#data.info()  #this line give you general info about the excel sheet inported (extra info not needed usualy). Number of rows/columns/etc...


#Step 2: Un commemt the line below and run. This will produce a file called 'data.json' to whereever your current python files are saved to.
#data.to_json("data.json")


#Step 3: Open the document created ('data.json') in last line of code and copy and paste it below after the equals sign in newDataFromJson.
null = 0
newDataFromJson = 
# Should be formatted as a nested dictionary... example: {"Name":{"0":"Samuel","1":"Eli","2":"Jacob","3":"Silas","4":"Gary","5":"Briana","6":"Tess","7":"Alyssa","8":"Karina","9":"Gianna","10":"Dan","11":"Jacob"},"Contact info":{"0":null,"1":"(978) 494-2645 ","2":null,"3":"(802) 825-2227","4":"(732) 801-5733","5":"(802) 734-9408","6":"(802) 760-8182","7":"(443) 848-1051","8":"(802) 282-6485","9":"(802) 777-6522","10":"(603) 562-7370","11":"(585) 857-1141"},"Unit":{"0":"66 Bradley","1":"66 Bradley","2":"66 Bradley","3":"64 Bradley","4":"65 Bradley","5":"66 Bradley","6":"64 Bradley","7":"64 Bradley","8":"64 Bradley","9":"66 Bradley","10":"66 Bradley","11":"66 Bradley"},"year\/s rented":{"0":"2021\/2022","1":"2021\/2022","2":"2021\/2022","3":"2021\/2022","4":"2021\/2022","5":"2021\/2022","6":"2020\/2021","7":"2020\/2021","8":"2020\/2021","9":"2019\/2021","10":"2019\/2021","11":"2019\/2021"}}

print('--------------')

#Step 4: change key value below to whatever you are looking up in excel table. Fill in number of row and columns based on output from data.info() in step 1.
rows = 12
columns = 4
key = '66 Bradley'
empty_array = []

for column in newDataFromJson:
    for i in range(0,rows-1,1):
        empty_array.append(newDataFromJson[column][str(i)])
print(empty_array)


if key in empty_array:
        print(newDataFromJson[column][str(i)])



#print(newDataFromJson['Name']['0'])

print('--------------')

dataflair_df = pandas.DataFrame(newDataFromJson)
print(dataflair_df)
