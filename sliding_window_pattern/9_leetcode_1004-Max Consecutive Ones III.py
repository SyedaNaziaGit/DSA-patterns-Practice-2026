'''
1004. Max Consecutive Ones III
Amazon has a cluster of n servers. '1' = ON, '0' = OFF.
Developers can flip a contiguous sequence of servers (ON→OFF or OFF→ON),
max k times. Find the maximum number of consecutive ON servers possible.

Example 1: server_states = "1001", k = 2 → Output: 4
(Flip the two 0s in 1 operation → "1111")

Example 2: server_states = "11101010110011", k = 2 → Output: 9
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #using two pointer approach to track number of 0s to flip i.e, k
        left = 0 #window pointer
        n = len(nums) #size of arr
        max_len = 0
        zero_count = 0
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0 :
                    zero_count -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len
    
s = Solution()
print(s.longestOnes(nums=  [1,1,1,0,0,0,1,1,1,1,0],k =2))#op - 6