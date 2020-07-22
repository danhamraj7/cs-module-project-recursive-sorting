# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case
    # find the target at midpoint or we deplete the range
    if start > end:
        return -1
        # else continue searching
    else:
        # find the mid point
        mid = (start + end) // 2
        # if the mid point match target return
        if arr[mid] == target:
            return mid
            #  recursive call to eliminate RHS. target is on LHS
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
            # recurse the  LHS
            # mid +1
        else:
            return binary_search(arr, target, mid + 1, end)

            # STRETCH: implement an order-agnostic binary search
            # This version of binary search should correctly find
            # the target regardless of whether the input array is
            # sorted in ascending order or in descending order
            # You can implement this function either recursively
            # or iteratively

            # def agnostic_binary_search(arr, target):
            #     # Your code here
