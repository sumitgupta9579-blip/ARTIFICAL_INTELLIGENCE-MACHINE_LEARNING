import numpy as np
Branch_a = [120, 150 ,180 ,100 ,200]
Branch_b = [80,130,170,120,150]

a = np.array(Branch_a)
b = np.array(Branch_b)

print(a)
print(b)

print("Total Inventory ",a+b)

print("Difference between ", abs(a-b))

aditional_a = a+20
aditional_b = b+20

print("Combined INventory ",aditional_a + aditional_b)

