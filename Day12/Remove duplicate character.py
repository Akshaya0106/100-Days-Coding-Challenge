def remove_duplicates(chars):
    slow = 0
    for fast in range(len(chars)):
        if chars[fast] not in chars[:slow]:
            chars[slow] = chars[fast]
            slow += 1
    return chars[:slow]

text = input("Enter a string: ")
chars = list(text)
result = remove_duplicates(chars)
print("Without duplicates:", "".join(result))

