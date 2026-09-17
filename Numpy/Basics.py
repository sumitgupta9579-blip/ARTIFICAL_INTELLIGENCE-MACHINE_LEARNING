import numpy as np 

# marks = [55,90,40,70,80]
# bonus = 5

# new_marks = []

# for m in marks:
#     new_marks.append(m+bonus)

# print(new_marks)

# Numpy -> Numerical python libraries provided by python used for performing mathematical operations 


marks = np.array([55,90,40,70,80])
bonus = 10

new_marks = marks + bonus

print(new_marks)

