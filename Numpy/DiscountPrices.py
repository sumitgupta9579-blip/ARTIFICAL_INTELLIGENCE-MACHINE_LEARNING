import numpy as np

Prices = np.array([100,250,400,550,800])
discount = Prices*0.10
discount_Prices = Prices-discount

print(Prices)
print(discount)
print(discount_Prices)