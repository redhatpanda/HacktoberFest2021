# Python 3 code to find sum


def _sum(arr):

    sum = 0

    for i in arr:
        sum = sum + i

    return sum


# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print("Sum of the array is ", ans)
