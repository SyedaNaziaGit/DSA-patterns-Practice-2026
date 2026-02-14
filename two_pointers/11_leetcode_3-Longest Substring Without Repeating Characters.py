'''
Docstring for two_pointers.11_leetcode_3-Longest Substring Without Repeating Characters
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
        char_set = set() #using  hashset to track current window and avoid duplicate
        #using sliding window and two pointers pattern 
        left =0 #first pointer
        max_length = 0 #max length of substring without repeating chars
        #maxlen of sliding window is length of string and right be second pointer iterating
        for right in range(len(s)):
            #if duplicate is encountered shrink window  from the left and remove duplicate element
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length,right + left -1)