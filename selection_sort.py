# 1. Create an unsorted array
myNums = [20, 83, 99, 28, 37, 45, 74, 16, 9, 35]
# 2. Create a function named selection_sort
def selection_sort():
    # 3. Create an iteration that will iterate with the array's length
    for i in range(len(myNums)):
        mins_index = i
        for j in range(i+1, len(myNums)):
        # 4. Compare the first element to the whole array to find the smallest value using another iteration
            if myNums[mins_index] > myNums[j]:
                mins_index = j
        # 5. If found, swap the two values. Repeat.
        myNums[i], myNums[mins_index] = myNums[mins_index], myNums[i]
    return myNums
# 6. Call the function
print(selection_sort())