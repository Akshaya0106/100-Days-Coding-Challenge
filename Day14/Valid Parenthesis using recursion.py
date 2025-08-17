def is_valid_recursion(s):
    if not s:
        return True
    if len(s) % 2 != 0:
        return False

    new_s = s.replace("()", "").replace("[]", "").replace("{}", "")

    if new_s == s:
        return False

    return is_valid_recursion(new_s)

print(is_valid_recursion("()[]{}"))
print(is_valid_recursion("(]"))
