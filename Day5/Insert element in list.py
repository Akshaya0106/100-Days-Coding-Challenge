size = int(input("Enter the size of array: "))
arr = [0] * size

print("Enter the elements:")
for i in range(size):
    arr[i] = int(input())

x = int(input("Enter the element to insert: "))
y = int(input("Enter the index to insert at: "))

new_arr = [0] * (size + 1)

for i in range(y):
    new_arr[i] = arr[i]

new_arr[y] = x

for i in range(y, size):
    new_arr[i + 1] = arr[i]

print("After insertion:")
for i in range(size + 1):
    print(new_arr[i], end=" ")