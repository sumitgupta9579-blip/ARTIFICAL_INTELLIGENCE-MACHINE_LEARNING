s = input("Enter a sentence: ")

names = s.split()

unique_names = []
vowel_count = 0
const_count = 0
digit_count = 0
space_count = 0

# Store unique names
for name in names:
        unique_names.append(name)

# Count characters
for ch in s:
    if ch.lower() in "aeiou":
        vowel_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == " ":
        space_count += 1
    elif ch.isalpha():
        const_count += 1

print("Unique Names:", unique_names)
print("Vowels:", vowel_count)
print("Consonants:", const_count)
print("Digits:", digit_count)
print("Spaces:", space_count)