'''
Docstring for two_pointers.15_leetcode-845-Longest Mountain in Array
You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
'''
from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #array should have atleast 3 elements to get the peak
        if len(arr)<3:
            return 0
        #building up array and down array
        up = [0] *len(arr)
        down = [0]*len(arr)
        #fill array up and down with the current array
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                up[i] = up[i-1] + 1
        for j in range(len(arr)-2, -1,-1):
            if arr[j]>arr[j+1]:
                down[j] = down[j+1]+1
        maxlen = 0
        for i in range(len(arr)):
            if up[i]>0 and down[i]>0:
                maxlen = max(maxlen,up[i] + down[i] + 1)
        return maxlen