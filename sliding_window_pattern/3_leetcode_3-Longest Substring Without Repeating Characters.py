'''
Docstring for 3_leetcode_3-Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using sliding window pattern
        #using set to avoid the duplicate substring
        char_set = set()#using hashset
        start = 0 #start of window
        max_length = 0 
        #iterating through the string chars and end being the end of the sliding window
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start]) #if  charset has the char already inside- to avoid duplicate
                start += 1 #moving forward
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1) #curr_window_size = end - start + 1
        return max_length
    #Time Complexity - O(n)