#!/usr/bin/python
import pandas as pd
car= pd.read_csv("Product_Sales_Data_Set.csv")
car
f = open('Iceberg-Cube-Results.txt','a+')
x=input("Enter the min")
print x
x1= str(x)
f.write(x1)
r=car.groupby('Item')['Sales_Units'].sum()
d=car.groupby(['Item','Location'])['Sales_Units'].sum()
t=car.groupby(['Year','Location','Item'])['Sales_Units'].sum()
print [r[r>x]]
print [d[d>x]]
print [t[t>x]]
h1 =str([r[r>x]])
z1= str([d[d>x]])
l1= str([t[t>x]])
f.write(h1)
f.write(z1)
f.write(l1)
f.close()








