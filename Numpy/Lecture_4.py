import numpy as np

# marks = np.array([70,80,65,90,75])

# print(marks.dtype)

# print(marks.ndim)

# print(marks.shape)

# print(marks.size)

marks = np.array([
    [72,85,90],
    [65,78,82],
    [88,91,84],
    [70,76,80]
])

print(marks[2])

print(marks[1,1])

marks[:,2] = marks[:,2] + 5

marks[3,0]=75

print(marks)
