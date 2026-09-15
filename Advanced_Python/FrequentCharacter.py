s = input("Enter a string: ")

char_count = {}

for ch in s:
    if ch != " ":           # Ignore spaces
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

max_char = max(char_count, key=char_count.get)

print("Character with maximum frequency:", max_char)
print("Frequency:", char_count[max_char])