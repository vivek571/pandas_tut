import pandas as pd

df=pd.read_csv(r"C:\Users\God\Downloads\PythonPrac\Jupyter\sample2.csv", index_col=['Roll No.'])
# print(df.head())
# print(df.loc[1])
# print(df.loc[[1,2,3,1]])
# print(df.loc[2, 'Physics'])
# print(df.loc[5:15, 'Chemistry'])

# print(df.loc[df['Physics']<50])

# print(df.loc[df['Physics']>80])

# print(df.loc[df['Physics']>80, 'Maths'])

# print(df.iloc[0])

# print(df.iloc[[0]])

# print(df.iloc[[0,1,2]])
print('*****')
print(df.head())

# print(df.iloc[:,0])
# print(df.iloc[:,1])
# print(df.iloc[0:5,1])
print(df.iloc[0:5, 1:4])


