def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter number of steps: "))
print("Number of ways to climb:", climbStairs(n))