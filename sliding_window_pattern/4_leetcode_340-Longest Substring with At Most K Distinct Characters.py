'''
Docstring for 4_leetcode_340-Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring that 
contains at most k distinct characters.
Example:
Input: s = "eceba", k = 2
Output: 3
Explanation: "ece"
'''
from typing import List
class Solution:
    def lengthOfLongestSubstringKDistinct(self,s: str,k: int): 
        #if k is 0 then number of distinct chars are 0
        if k == 0:
            return 0
        #using sliding window pattern
        start = 0 #start of the window
        max_len = 0
        char_count = {}#using hashmap for checking the charcount to find the k distinct char
        for end in range(len(s)):
            char_count[s[end]]= char_count.get(s[end],0)+1
            # Shrinking window if distinct chars > k
            while len(char_count) >k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    del char_count[s[start]] #removing char
                start += 1
            max_len = max(max_len,end-start+1)#curr_window_size = end - start + 1
        return max_len
s= Solution()
print(s.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))