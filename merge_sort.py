# 1. Create an unsorted array
myNums = [20, 83, 99, 28, 37, 45, 74, 16, 9, 35]
# 2. Create a function named merge_sort
def merge_sort(myNums):
# 3. Divide the array until only one single element is left
    arr_len = len(myNums)
    if arr_len > 1:
        half = arr_len//2
        L_arr = myNums[:half]
        R_arr = myNums[half:]
        merge_sort(L_arr)
        merge_sort(R_arr)
        i = j = k = 0 # indexes
# 4. sort the groups recursively.
        while i < len(L_arr) and j < len(R_arr):
            if L_arr[i] < R_arr[j]:
                myNums[k] = L_arr[i]
                i += 1
            else:
                myNums[k] = R_arr[j]
                j += 1
            k += 1
        while i < len(L_arr):
            myNums[k] = L_arr[i]
            i += 1 
            k += 1 
        while j < len(R_arr):
            myNums[k] = R_arr[j]
            j += 1 
            k += 1 
# 5. return the array
    return myNums
# 6. call the function
print(merge_sort(myNums))
