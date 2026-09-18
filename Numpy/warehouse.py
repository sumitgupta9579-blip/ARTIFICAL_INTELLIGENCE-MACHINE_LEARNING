import numpy as np

array = np.full((4,5),100)

print(array)
print()

array[:2,:] = array[:2,:] + 20

print(array)
print()

array[:,-2:] = array[:,-2:]*0.90

print(array)
print()

print(array[1:3,:])
print()

print(array[: ,:3])
print()

print(array[-2:,-2:])