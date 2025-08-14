n1 = int(input("Enter number of elements in first sorted list: "))
list1 = []
for _ in range(n1):
    num = int(input())
    list1.append(num)

n2 = int(input("Enter number of elements in second sorted list: "))
list2 = []
for _ in range(n2):
    num = int(input())
    list2.append(num)

i = j = 0
merged = []

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged sorted list:", merged)


