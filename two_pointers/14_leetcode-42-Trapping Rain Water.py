'''
Docstring for two_pointers.14_leetcode-42-Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water_level = 0
        #using two pointer approach 
        left = 0 #first pointer pointing at start  of array
        right = len(height) -1 # second pointer pointing at end of the array
        #water can sit between mininum of left max height and right max height minus currentheight
        #tracking max left height and max right height and finding water level at each
        left_max , right_max = 0, 0
        #iterating through array
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_level += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_level += right_max - height[right]
                right -= 1
        return water_level