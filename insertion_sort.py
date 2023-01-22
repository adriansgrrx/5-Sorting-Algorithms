# 1. Create an unsorted array
myNums = [20, 83, 99, 28, 37, 45, 74, 16, 9, 35]
# 2. Create a function named insertion_sort
def insertion_sort():
# 3. Create a for loop that will iterate the array with respect to its length
    for i in range(1, len(myNums)):
        element = myNums[i] #i = 1
        j = i-1 # 0
# 4. Create a while loop that will compare a consecutive pair in the array
        while j >= 0 and element < myNums[j]: # greater than index 0
            myNums[j+1] = myNums [j]
            j -= 1
        myNums[j+1] = element
# 5. return the array
    return myNums
# 6. call the function
print(insertion_sort())