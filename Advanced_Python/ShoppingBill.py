item=[]
price=[]
for i in range(5):
    item.append(input("Enter the item name :"))
    price.append(int(input("Enter the price of item :")))
print("Total bill of items is :",sum(price))
print("Highest price of item is :",max(price))
print("Lowest price of item is :",min(price))
