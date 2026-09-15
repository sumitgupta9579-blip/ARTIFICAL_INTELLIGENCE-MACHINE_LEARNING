num=[1,2,3,4,5]
square=[]
for i in num:
    square.append(i*i)

# print(square)


square = list(map(lambda x:x**2,num))
# print(square)


def sq(x):
    return x*x
# print(sq(5))


sq = lambda x: x*x
# lambda parameters : expression


twice = lambda x:2*x
# print(twice(15))


sum=lambda x,y:x+y
# print(sum(4,5))



def max(x,y):
    if(x>y) : return x
    else : return y

# print(max(48,54))


max = lambda x,y:x if x>y else y
# print(max(48,54))


def check(x):
    if(x%2==0) : return "even"
    else: return "odd"

num = lambda x:"even" if x%2==0 else "odd"
print(num(51))


last_char = lambda x:x[-1]
print(last_char("sumit"))


product = lambda x,y,z:x*y*z

print(product(4,2,8))