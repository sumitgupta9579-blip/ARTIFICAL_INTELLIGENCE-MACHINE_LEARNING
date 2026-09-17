import numpy as np

company_rec = np.array([125000 , 148000 , 135000 , 1720000])
print("Company Records ",company_rec)

higher = company_rec*0.15
print("Higher 15% sales " , higher)

excepted_sales = company_rec + higher 
print("Excepted Sales ",excepted_sales)

next_year_sales_req =  excepted_sales - company_rec 
print("next_year_sales_req " , next_year_sales_req)


