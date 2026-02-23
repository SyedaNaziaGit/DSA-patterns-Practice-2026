'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #using sliding window pattern and frequency counter from collections to get count of each char in str
        s1_freq_count = Counter(s1)
        window_freq_s2 = Counter(s2[:len(s1)])
        if s1_freq_count == window_freq_s2:
            return True
        left = 0
        #moving the window
        for right in range(len(s1),len(s2)):
            window_freq_s2[s2[right]] += 1
            #maintain window size
            if right - left +1 > len(s1):
                window_freq_s2[s2[left]] -= 1
                if window_freq_s2[s2[left]] == 0:
                    del window_freq_s2[s2[left]]
                left += 1
            #comparing counts
            if window_freq_s2 == s1_freq_count:
                return True
        return False
        