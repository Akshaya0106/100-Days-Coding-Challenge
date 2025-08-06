def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

n = int(input("Enter number of elements: "))
arr=[]
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

insertion_sort(arr)
print("Sorted array:", arr)
