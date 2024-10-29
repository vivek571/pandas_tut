import pandas as pd
#Replace

df=pd.read_csv(r"C:\Users\God\Downloads\PythonPrac\Jupyter\sample.csv")
print(df.head)

df1=df.replace(to_replace=26, value=999999)
print(df1)

df2=df.replace(999999, 26)
print(df2)

df3=df.replace(to_replace=[50,51,52,53], value='AAAAAA')
print(df3)

df4=df.replace(to_replace=[50,51,52,53], value=['50ABC', '51ABC', '52ABC', '53ABC'])
print(df4)

df5=df['Physics'].replace(to_replace=[50,51,52,53], value=['A','B','C','D'])
print(df5)



print(df4)
df6=df4.replace('[A-Za-z]',0, regex=True)
print(df6)



