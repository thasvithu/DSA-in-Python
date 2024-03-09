# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:22:16 2024

@author: vithu
"""

def bubble_sort(arr):
    size = len(arr)
    
    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            

if __name__ == "__main__":
    nums = [8, 1, 5, 7, 3, 12, 11]

    print("Before Sorting ", nums)

    bubble_sort(nums)
    print("After Sorting ", nums)

    
    

