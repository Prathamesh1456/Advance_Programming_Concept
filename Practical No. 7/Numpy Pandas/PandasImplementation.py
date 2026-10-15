import pandas as pd
#Add character label to array
nums=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# print(nums)


#create series with .csv file
# data=pd.read_csv('student.csv')
# print(data)

#Create dataframe with .CSV file


df = pd.read_csv('student.csv')
print(df.head())
# print(df.head())

