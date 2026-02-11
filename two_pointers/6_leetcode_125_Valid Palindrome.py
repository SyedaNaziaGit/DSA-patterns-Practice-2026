'''
Docstring for two_pointers.6_leetcode_125_Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right = 0, len(s)-1
        #iterating throughthe string
        while left < right:
            #skipping alphanumeric characters in a string
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            #comparing case insensitivity of char
            if s[left].islower() != s[right].islower():
                return False
            left += 1
            right -= 1
        return True