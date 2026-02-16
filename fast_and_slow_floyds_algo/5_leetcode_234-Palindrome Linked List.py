'''
Docstring for 5_leetcode_234-Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
'''
from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #if linked list is empty or single element then its true
        if not head and not head.next:
            return True 
        #here we need three steps -  
        # finding mid element , reversing the other half of linkedlist and 
        # comparing two halves are equal
        #1.using floyd's algo finding mid of the linkedlist
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Here slow is at  mid point when fast is at end
        #2.reversing the other half another  pointer
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev= slow
            slow = temp
        #3. comparing halvess
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False#not palindrome
            left = left.next
            right = right.next
        return True #palindrome
    #Time Complexity - O(n) and Space Complexity - O(1)