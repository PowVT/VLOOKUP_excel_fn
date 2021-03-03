## VLOOKUP ##
## BY: PowVT ###
## circa 2021 ##

#This script emulates the excel function VLOOKUP (value, table, col_index, [range_lookup])
#Follow the steps below to

import pandas as pandas
import numpy as np
import json

#step 1: copy and paste excel file path into parentheses on next line. include full file path
data = pandas.read_excel (r'***insert_file_path_here***')
#data.info()  #this line give you general info about the excel sheet inported (extra info not needed usualy). Number of rows/columns/etc...


#Step 2: Un commemt the line below and run. This will produce a file called 'data.json' to whereever your current python files are saved to.
#data.to_json("data.json")


#Step 3: Open the document created ('data.json') in last line of code and copy and paste it below after the equals sign in newDataFromJson.
# A sample of what this should look like is shown below.
null = 0
newDataFromJson = {"Name":{"0":"Samuel Leo","1":"Eli Stein","2":"Jacob Decatur","3":"Silas Goldman","4":"Gary Krall","5":"Briana Benoit","6":"Tess","7":"Alyssa","8":"Karina","9":"Gianna","10":"Dan","11":"Jacob"},
                   "Contact info":{"0":null,"1":"(978) 494-2645 ","2":null,"3":"(802) 825-2227","4":"(732) 801-5733","5":"(802) 734-9408","6":"(802) 760-8182","7":"(443) 848-1051","8":"(802) 282-6485","9":"(802) 777-6522","10":"(603) 562-7370","11":"(585) 857-1141"},
                   "Unit":{"0":"66 Bradley","1":"66 Bradley","2":"66 Bradley","3":"64 Bradley","4":"65 Bradley","5":"66 Bradley","6":"64 Bradley","7":"64 Bradley","8":"64 Bradley","9":"66 Bradley","10":"66 Bradley","11":"66 Bradley"},
                   "year\/s rented":{"0":"2021\/2022","1":"2021\/2022","2":"2021\/2022","3":"2021\/2022","4":"2021\/2022","5":"2021\/2022","6":"2020\/2021","7":"2020\/2021","8":"2020\/2021","9":"2019\/2021","10":"2019\/2021","11":"2019\/2021"}}
#Top level: Name, Contact Info, Unit, Years Rented
#Sub level: 0,1,2,3,4,5,6,7,8,9,10,11


print('--------------')

#Step 4: change key value below to whatever you are looking up in excel table.
# Fill in number of rows and columns based on output from data.info() in step 1.
# Fill in lookup value, this is the column in your raw data that you want to grab the key values corresponding info from.

rows = 12
columns = 4
key = '66 Bradley'
lookup = 'Name'
empty_array = []

for column in newDataFromJson:
    for i in range(0,rows,1):
            if newDataFromJson[column][str(i)] == key:
                empty_array.append(newDataFromJson[lookup][str(i)])
print(empty_array)


#if key in empty_array:
    #print(newDataFromJson[column][str(i)])


#print(newDataFromJson['Name']['0'])

print('--------------')

#dataflair_df = pandas.DataFrame(newDataFromJson)
#print(dataflair_df)
