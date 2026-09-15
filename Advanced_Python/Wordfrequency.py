sen=input("Enter a sentence :")
words=sen.split(" ")
dict={}
for ele in words:
    if(ele not in dict):
        dict[ele]=1
    else:
        dict[ele]+=1
print(dict)