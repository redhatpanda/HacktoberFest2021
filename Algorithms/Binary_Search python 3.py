#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def binary_search(arr, n):  # Declaring Function named binary search
    start = 0  # Creating a start
    end = len(arr)  # Creating an end which will be the length of the list
    arr.sort()  # As it is mandatory that the given list should be sorted
    while start <= end:  # Obvious condtion
        k = (
            start + end
        ) // 2  # Creating a variable which will reject half of the list according to the 'n':element to be find
        if (
            arr[k] > n
        ):  # Checking that whether the element in the middle is greater than the number to be find
            end = (
                k - 1
            )  # If the middle element tis greater than the N:Element to be find then push end towards (middle -1) index
        elif (
            arr[k] < n
        ):  # If the converse of the earlier condition happened then shifting the middle number according to it
            start = k + 1
        elif (
            arr[k] == n
        ):  # If the middle number and the number to be find collioded then return the index of the middle number
            return k  # Returning the index
    return -1  # Else returning -1 which indicates that element is not present


arr = [int(x) for x in input().split()]  # List comprehension for taking the input
n = int(
    input("Enter the element to be find ")
)  # Taking the input of the Element to be find
res = binary_search(arr, n)  # Calling the function and filling the argument
print(res)  # Printing result
