'''
Docstring for two_pointers.7_leetcode_977- Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
'''
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #return sorted([(i*i) for i in nums])- this solution will take time complexity of O(nlogn)
        #using two pointers appraoch we can get the Time Complexity - O(n) and Space Complexity -  O(n)
        n = len(nums)
        res = [0]*n
        left,right = 0,n-1
        #choosing another pointer to sort pointed at end of array
        position = n-1
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square > right_square:
                res[position] = left_square
                left += 1
            else:
                res[position] = right_square
                right -= 1
            position -= 1
        return res
        