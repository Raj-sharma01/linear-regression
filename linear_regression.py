import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
data=pd.read_csv('Salary_dataset.csv')

x=data['YearsExperience']
y=data['Salary']
n=len(y)
print(y[0])

print(x.dtype,y.dtype)

# update the value of m and b 
def grad_decent(m,b,l):
    m_grad=0
    b_grad=0
    for i in range(1,n):
       m_grad+=(-2/n)*(x[i]*(y[i]-(m*x[i]+b)))
       b_grad+= (-2/n)*(y[i]-(m*x[i]+b))

    m=m-m_grad*l  
    b=b-b_grad*l   

    return (m,b)

epoc=1000
l = 0.0001 #learning rate

m=0
b=0
for i in range(epoc):
    m,b=grad_decent(m,b,l)

plt.scatter(data.YearsExperience, data.Salary)
plt.plot(data.YearsExperience, m *data.YearsExperience + b, color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()



