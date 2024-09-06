#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def merge(arr, s , e):
    mid = (s+e)//2
    left_arr = arr[s:mid+1]
    right_arr = arr[mid+1:e+1]

    index_left , index_right, main_index = 0, 0, s
    inv_count=0

    while(index_left<len(left_arr) and index_right<len(right_arr)):
        if left_arr[index_left] <=right_arr[index_right]:
            arr[main_index] = left_arr[index_left]
            index_left+=1
        else:
            arr[main_index] = right_arr[index_right]
            inv_count += len(left_arr)-index_left
            index_right+=1
        main_index+=1

    while(index_left<len(left_arr)):
        arr[main_index]= left_arr[index_left]
        main_index+=1
        index_left+=1

    while(index_right<len(right_arr)):
        arr[main_index]= right_arr[index_right]
        main_index+=1
        index_right+=1

    return inv_count

def merge_sort(arr, s, e):
    if s>=e:
        return 0

    mid = (s+e)//2
    inv_count=0
    inv_count +=merge_sort(arr, s, mid)
    inv_count +=merge_sort(arr, mid+1, e)
    inv_count +=merge(arr, s, e)

    return inv_count

def countInversions(arr):
    return merge_sort(arr, 0, len(arr)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
