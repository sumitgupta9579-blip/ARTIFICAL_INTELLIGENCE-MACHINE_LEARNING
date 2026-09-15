dict={}
for i in range(5):
    key=input("Enter player name :")
    value=int(input("Enter player runs :"))
    dict[key]=value

name = max(dict, key=dict.get)
score = sum(dict.values()) / len(dict)
print("Higher Scorer ",name)
print("Average Score",score)

