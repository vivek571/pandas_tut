import pandas as pd

df=pd.read_csv(r"C:\Users\God\Downloads\PythonPrac\Jupyter\sample.csv")
# print(df.head())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

#Dropping rows with Nan
print(df.shape)

df1=df.dropna(axis=0) #default axis = 0
print(df1.shape)

df2=df.dropna(axis=1)
print(df2.shape)

df3=df.dropna(how='any')    #remove any row having a null value
print(df3.shape)
print(df3.size)

df4=df.dropna(how='all')    #remove row if all values are null
print(df4.shape)
print(df4.size)

df.dropna(inplace=True)
