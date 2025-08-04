class Search:
    def __init__(self, data):
        self.data = data

    def binary_search(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.data[mid] == target:
                print(f"{target} found")
                return
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        print(f"{target} not found")


size = int(input("Enter number of elements: "))
print("Enter elements:")
arr = []
for _ in range(size):
    num = int(input())
    arr.append(num)

target = int(input("Enter the number to search: "))

s = Search(arr)
s.binary_search(target)
