# 1. Create an unsorted array
myNums = [20, 83, 99, 28, 37, 45, 74, 16, 9, 35]
# 2. Create a function named merge_sort
def quick_sort(arr):
# 3. Select a pivot
    # to select a pivot, we need to divide the array
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
# 4. distribute the elements by left(less than) and right (greater than than pivot)
    left = []
    for element in arr:
        if element < pivot:
            left.append(element)

    middle = [] #pivot
    for element in arr:
        if element == pivot:
            middle.append(element)

    right = []
    for element in arr:
        if element > pivot:
            right.append(element)
# 5. return sorted sort the array
    sorted_array = quick_sort(left) + middle + quick_sort(right)
    return sorted_array
# 6. call the function
print(quick_sort(myNums))