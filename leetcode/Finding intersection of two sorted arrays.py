import bisect

def intersection_two_sorted(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return []


    res = []

    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            ptr1 += 1
        elif arr1[ptr1] > arr2[ptr2]:
            ptr2 += 1
        else:
            res.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1

    return res


print intersection_two_sorted([1,4,6,10], [-3, -2, 2, 4 ,10, 12])