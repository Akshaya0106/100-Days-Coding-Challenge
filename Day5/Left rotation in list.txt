arr = [0] * 10
print("Enter 10 elements:")
for i in range(10):
    arr[i] = int(input())

n = int(input("Enter number of left rotations: "))
length = 10

for _ in range(n):
    first = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = first

print("After left rotation:")
for i in range(length):
    print(arr[i], end=" ")