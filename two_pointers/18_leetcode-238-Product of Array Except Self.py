'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        #instead of divide and compute- calculation prefix product and suffix product
        #prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        #suffix product
        suffix = 1
        for i in range((n-1),-1,-1):
            result[i] = suffix
            suffix *= nums[i]
        return result