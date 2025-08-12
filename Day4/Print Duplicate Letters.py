def find_repeating_letters(s):
    counts = {}
    duplicates = []
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1 and char!=' ':
            duplicates.append(char)
    return duplicates

my_string =input("Enter a string:")
repeating_letters = find_repeating_letters(my_string)

print(f"The string is: '{my_string}'")
print(f"The repeating characters are: {repeating_letters}")