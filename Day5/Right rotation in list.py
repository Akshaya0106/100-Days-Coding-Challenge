arr = [0] * 10
print("Enter 10 elements:")
for i in range(10):
    arr[i] = int(input())

n = int(input("Enter number of right rotations: "))
length = 10

for _ in range(n):
    last = arr[length - 1]
    for i in range(length - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

print("After right rotation:")
for i in range(length):
    print(arr[i], end=" ")