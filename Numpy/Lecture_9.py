import numpy as np

# marks = np.array([45,72,88,31,65,90])

# use where like if-else np.where(condition , value_if_true , value_if_false )

# print(np.where(marks > 70 , "Good" , "Average"))

# n_m = np.where(marks < 50 , marks + 5 , marks)

# print(n_m)

# demo = np.where(marks > 50 , np.where(marks < 89 , "pass" , "Excellent") , "fail")

# print(demo)

salary = np.array([60000 , 40000 , 75000 , 55000 , 30000])
credit_score = np.array([720 , 750 , 680 , 710 , 800])

loan_Status = np.where(salary >= 50000 ,np.where(credit_score >=700 , "Approved" , "Reject")  , "Reject")

print(loan_Status)