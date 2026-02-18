'''
Docstring for 1_leetcode_643-Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #using sliding window pattern - with k as window to find the max average
        window_sum = sum(nums[:k]) #finding  starting maxsum as window sum
        max_sum = window_sum
        for i in range(k,len(nums)):
            window_sum += nums[i] #moving to next element 
            window_sum -= nums[i-k] #removing previous element
            max_sum = max(max_sum,window_sum)
        return max_sum/k #average of max_sum