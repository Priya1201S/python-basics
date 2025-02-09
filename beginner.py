'''a="ramram"
mid=len(a)//2
if a[:mid]==a[mid:]:
    print("the number is symmetrical")'''
    


'''name="ada"
if name[0:]==name[-1]:
   print("the number is pallindrome")'''



'''p="i am priya"
if "pra"in p:
    print("yes")
else:
   print("no")


import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# Creating the bar plot
plt.bar(courses, values, color='maroon', width=0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
n=int(input('Enter n value:')) 
for i in range(n): 
   print('*',end=' ')
n=int(input('Enter n value:')) 
for i in range(n): 
   print('*',end=' ')
n=int(input('Enter No Of Rows:')) 
for i in range(n): 
   print('* '*n)
import pandas as pd 
d={"name":["priya","neha"],"age":[19,35]}
df=pd.DataFrame(data=d)
print(df)
df.set_index("name",inplace=True)
result=df.loc["priya"]
print(result)


import pandas as pd

d=[1,2,2,5,3,6.5]

a=pd.Series(d)

print(a)

a.value_counts(bins=2)

a,b= [int(x) for x in input("Enter 2 numbers :").split()] 
print("Product is :", a*b)


n = int(input("Enter number of rows:"))
for i in range(1,n+1): 
 for j in range(1,i+1): 
    print("*",end=" ") 
 print() 
n = int(input("Enter number of rows:"))
for i in range(1,n+1): 
   print("* " * i)'''
n = int(input("Enter number of rows:"))
for i in range(1,n+1): 
 print(" " * (n-i),end="") 
 print("* "*i) 
