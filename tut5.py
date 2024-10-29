import pandas as pd

df=pd.read_csv(r"C:\Users\God\Downloads\PythonPrac\Jupyter\sample.csv")
# print(df.head())

#Filling the NA
# print(df.isnull().sum())
# df1=df.fillna(0)
# print(df1.isnull().sum())
# print(df1.head)

# #Filling specific values
# df2=df.fillna(
#     {
#         'Physics':'None', 'Chemistry':0, 'Maths':9999
#     })
# # print(df2)
# print(df2.head)

# #Forward fill
# df3=df.fillna(method='ffill')
# print(df3)

# df4=df.fillna(method='ffill', axis=1)
# print(df4)

df5=df['Physics'].fillna(value=df['Physics'].mean())
print(df5)































