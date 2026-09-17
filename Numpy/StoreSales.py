import numpy as np

prices = np.array([250,400,750,1200])

unit_sold = np.array([12,8,5,10])

revenue = prices*unit_sold

print(revenue)

revenue_increase = revenue*0.05

revenue = revenue+revenue_increase

print(revenue_increase)

print(revenue)