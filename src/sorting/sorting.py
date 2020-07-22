# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # * merged_arr - contains arr of zeros - whatever length of arrA and arrB
    merged_arr = [0] * elements
    # start the pointers at begining of both list
    a, b = 0, 0
    # loop through the merged arr * merged_arr
    for i in range(len(merged_arr)):
        # compare the values at both pointers
        # which ever value is smaller copy to merged
        # list(ie. copy that contains the both list that is being merged)
        # increment the pointer to move to the next one
        # Your code here
        # check if the pointers is out of bounds of its respective array
        # if so copy over every element from the other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            # both indicies are still out of bounds in their respective arrays
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            # only other case
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # break the arr down recursively
    # base case:  when the the lists gets to length 1
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
