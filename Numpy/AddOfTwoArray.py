# Using Numpy

import numpy as np 
a = [3,5,6]
b = [5,6,1]

an = np.array(a)
bn = np.array(b)

# print(an+bn)


# Using Python

c = []

n=len(a)

for i in range(n):
    c.append(a[i]+b[i])

# print(c)

a = np.arange(0,11,2)
print(a)

b = np.linspace(0,10,6)
print(b)


c = np.array([10.5, 20.7 , 30.3],dtype = int)
print(c)
print(c.dtype)