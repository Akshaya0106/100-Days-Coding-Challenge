class Search:
    def __init__(self, data):
        self.data = data

    def linear_search(self, target):
        for i in range(len(self.data)):
            if self.data[i] == target:
                print(f"{target} found")
                return
        print(f"{target} not found")

size = int(input("Enter number of elements: "))
print("Enter element: ")
arr = []
for _ in range(size):
    num = int(input())
    arr.append(num)

target = int(input("Enter number to search: "))

s = Search(arr)
s.linear_search(target)


