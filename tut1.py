import pandas as pd

print(pd.__version__)

lst = [1,2,3,4,5,6]

series = pd.Series(lst)
print(series)
print(type(series))

empty = pd.Series([])
print(empty)

a = pd.Series(['p', 'q','r','s','t'], index = [11,12,13,14,15])
print(a)

a = pd.Series(['p', 'q','r','s','t'], index = [11,12,13,14,15], name='alphabest')
print(a)

sclar_series = pd.Series(0.5, index=[1,2,3])
print(sclar_series)

dict_series = pd.Series(
    {
        'p': 1,
        'q': 2,
        'r': 3
    }
)
print(dict_series)

print(dict_series[0])
print(dict_series.iloc[0])
print(dict_series.iloc[1:3])
print(max(dict_series))

dict_series = pd.Series(
    {
        'p':[1,2,3],
        'q':[3,4,5],
        'r':[5,6]
    }
)
print(dict_series)