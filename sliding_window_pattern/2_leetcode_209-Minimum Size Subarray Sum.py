'''
Docstring for 2_leetcode_209-Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #using sliding window pattern
        curr_sum = 0
        start = 0 #start of window
        min_len = float('inf')
        #iterating through array with end being end of window
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_len = min(min_len, end - start + 1)#end-start+1 is current window
                curr_sum -= nums[start] #removing the start pointer element - moving forward
                start += 1 #moving forward the start of the window
        return 0 if min_len == float('inf') else min_len