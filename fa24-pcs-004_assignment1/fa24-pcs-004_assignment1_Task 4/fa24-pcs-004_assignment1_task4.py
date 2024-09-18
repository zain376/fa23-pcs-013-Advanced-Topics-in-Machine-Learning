import pandas as pd
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}

custom_dataframe = pd.DataFrame(data)
custom_dataframe.head(2)
custom_dataframe['C2']
custom_dataframe.rename(columns={'C3':'B3'})
custom_dataframe['Sum'] = 0
custom_dataframe['Sum']= custom_dataframe[['C1', 'C2', 'C3', 'C4']].sum(axis=1)
custom_dataframe

dataframe = pd.read_csv('hello_sample.csv')
print(dataframe)

dataframe.tail(2)

dataframe.info()
dataframe.shape


sorted_dataframe = dataframe.sort_values(by='Weight', ascending=True)
sorted_dataframe

sorted_dataframe.isnull()

sorted_dataframe.dropna()