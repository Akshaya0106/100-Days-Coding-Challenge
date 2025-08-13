def length_of_longest_substring(s):
    left = 0
    max_length = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
s=input("Enter a string:")
print(length_of_longest_substring(s))