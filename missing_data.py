import pandas as pd

wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")

#Uncomment the print statements as needed!

#Find unique data
# print(wh["Snow depth (cm)"].unique())

#Get null mask
# print(wh.isnull())   


#Find all rows that have missing values
#wh[wh.isnull().any(axis=1)]

#dropna for columns
#wh.dropna().shape

#dropna for rows
# wh.dropna(axis=1).shape

#dropna with threshold i.e. how many empty values do you need to drop a row/column?
# wh.dropna(thresh = 3) 

