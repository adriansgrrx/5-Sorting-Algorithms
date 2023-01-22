# 1. Create an unsorted array
myNums = [20, 83, 99, 28, 37, 45, 74, 16, 9, 35]
# 2. Create a function named bubble_sort
def bubble_sort():
# 3. Get the length of the array
    l = len(myNums)
    for i in range(l):
# 4. Traverse the array from 0 to n-i-1
    # Swap if the element found is greater
    # than the next element
        for j in range(0, l-i-1):
            if myNums[j] > myNums[j+1]:
                myNums[j], myNums[j+1] = myNums[j+1], myNums[j]
    return myNums
# 5. Call the function
print(bubble_sort())