'''
Docstring for two_pointers.8_leetcode-713-Subarray Product Less Than K
ven an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2: 
Input: nums = [1,2,3], k = 0
Output: 0
'''
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        #using two pointer sliding window  to get the subarray and finding the product
        product = 1 # product cannot be less than 1
        left =0 #fixing left pointer
        count = 0 # count of the subarrays whose product is <k
        #moving right pointer 
        for right in range(len(nums)):
            #product while expanding  window
            product *= nums[right]
            #check if product >=k then  we shrink window
            while product >= k:
                #divide while shrinking the subarray / window moving left pointer
                product //= nums[left]
                left += 1 #shrinking left pointer
            #number of valid subarrays with formula as right-left+1
            count += right - left + 1
        return count
        
