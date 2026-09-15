str=input("Enter a string: ")
new_s=""
for ch in str:
    if ch <= "z" and ch >= "a":
        new_s += chr(ord(ch)-32)
    else:
        new_s +=ch
print(new_s)