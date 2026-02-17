'''
Docstring for 7_leetcode_287-Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
'''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using two pointer approach and floyds algo
        #considering list as linkedlist as the nums range from 1 to n
        #each index points to num[index] - a cycle may exists- pigeonhole principle. i.e, n+1 numbers,n possible values
        #at least one number should repeat -  then we have duplicate
        
        #detect cycle using two pointers approach - floyds algo
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow] #move pointer one step
            fast = nums[nums[fast]] #move poinetr two steps
            if slow == fast:
                break #  cycle is deteced
        #to find the entry point for the cycle
        while slow != fast:
            slow = nums[slow] #move pointer one step
            fast = nums[fast] #move pointer one step
        return slow 