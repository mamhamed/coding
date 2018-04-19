"""
Generate all possible subset of size r of given array with distinct elements.
https://www.geeksforgeeks.org/print-subsets-given-size-set/
"""

def subsets(arr, k):
    if len(arr) < k:
        return [[]]

    if len(arr) == k:
        return [arr]

    if k == 1:
        return [[x] for x in arr]

    return subsets(arr[1:], k) + [[arr[0]]+x for x in subsets(arr[1:], k-1)]


print subsets([1,2,3,4], 2)
print subsets([10,20,30,40,50], 3)