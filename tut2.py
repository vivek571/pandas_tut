import pandas as pd

df=pd.DataFrame()
print(df)

lst = [1,2,3,4,5,6]
df=pd.DataFrame(lst)
print(df)

lst=[[1,2,3,4,5], [11,12,13,14,15,16]]
df=pd.DataFrame(lst)
print(df)

a=pd.DataFrame(
    {
        'p':[1,2,3],
        'q':[3,4,5],
        'r':[5,6,7],
        's':[7,8,9],
        't':['a','b','c']
    }
)
print(a)

b=pd.DataFrame(
    {
        'RollNo':pd.Series([1,2,3,4]),
        'Maths': pd.Series([10,12,14,16,17,18]),
        'Physics':pd.Series([0.1,90,91])
    }
)
print(b)
print(type(b))

df=pd.read_csv(r"C:\Users\God\Downloads\PythonPrac\Jupyter\marks.csv")
print(type(df))