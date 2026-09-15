# map(function,iterable) --> it returns a map object --> convert it into list -->list(map(lambda ))

# cube=[]
# def fun(lst):
#     for i in lst:
#         cube.append(i**3)
#     return cube

# print(fun(lst=[1,2,4,8]))


# def cb(i):
#     return i**3
# cube = []
# lst = [4,6,2]
# for ele in lst:
#     cube.append(cb(ele))
# print(cube)


# lst=[4,6,2]
# cube = list(map(lambda x:x**3,lst))
# print(cube)


# lst=[1,2,3,4,5]
# add=list(map(lambda x:x+5,lst))
# print(add)

s=["Sumit","Pravin","Swapnil","sahil"]
# ups=[]
# for ele in s:
#     ups.append(ele.upper())

# print(ups)


# ss=["s","u","m","i","t"]
# upper=list(map(lambda s:s.upper(),ss))
# print(upper)

lst = [100,150,200,250,300,500]
gst=list(map(lambda x:x+x*18/100,lst))
print(gst)


        