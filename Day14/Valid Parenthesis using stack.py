def is_valid_stack(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0

print(is_valid_stack("()[]{}"))
print(is_valid_stack("(]"))
