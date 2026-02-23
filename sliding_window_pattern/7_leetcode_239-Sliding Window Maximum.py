'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.
Return the max sliding window.
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
from typing import  List
from collections  import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        #using sliding window pattern along with deque - monotonic decreasing deque -max is at front
        #to efficiently track the maximum-  
        # expand the window with right pointer- say end  and removing elements getting out of range
        for end in range(len(nums)):
            #removing elements outside window
            while dq and dq[0] <= end - k:
                dq.popleft()
            #maintaining decreasing order
            while dq and nums[dq[-1]] <  nums[end]:
                dq.pop()
            dq.append(end)
            #window formed
            if end >= k - 1:
                result.append(nums[dq[0]])
        return result