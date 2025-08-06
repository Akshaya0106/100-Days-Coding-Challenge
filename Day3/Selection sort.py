def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Sorted:", selection_sort(arr))
