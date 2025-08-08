size = int(input("Enter the size of array: "))
arr = [0] * size

print("Enter the elements:")
for i in range(size):
    arr[i] = int(input())

index = int(input("Enter the index to delete: "))

new_arr = [0] * (size - 1)

for i in range(index):
    new_arr[i] = arr[i]

for i in range(index + 1, size):
    new_arr[i - 1] = arr[i]

print("After deletion:")
for i in range(size - 1):
    print(new_arr[i], end=" ")