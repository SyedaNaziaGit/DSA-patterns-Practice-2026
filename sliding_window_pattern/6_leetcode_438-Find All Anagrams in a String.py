'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #using fixed sliding window  pattern
        #edge case
        if len(p) > len(s):
            return []
        #base case
        result = []
        count = [0]*26 #fixed size window of 26 chars
        #slide window of length p over s
        #when the window size = len of p and frequencies matches, store left index
        
        #getting count frequencyof chars in p
        for ch in p:
            count[ord(ch) - ord('a')] += 1
        
        #left pointer of window
        left = 0
        for right in range(len(s)):
            #include current character
            count[ord(s[right]) - ord('a')] -= 1
            #if count goes negative , then shrink window
            while count[ord(s[right]) - ord('a')] < 0:
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            #if window size matches
            if right-left+1 == len(p):
                result.append(left)
        return result
    #Time Compelxity- O(n) and Space Complexity - O(1)