'''
Docstring for 6_leetcode_19-Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''
#class for singly linkedlist
from typing import Optional
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #using two pointer approach 
        #taking dummy node so that if we have to remove head its tricky
        dummy = ListNode(0) #creating a linkedlist
        dummy = head #keep a copy of head as dummy
        #using floyd's algo of slow and fast pointer approach to remove nth node
        slow = dummy
        fast = dummy
        #moving fast pointer n steps
        for _ in range(n):
            fast = fast.next
        #moving both slow  and fast pointer one step till fast reaches end, so that slow pointer is before nth node to be deleted
        while fast.next:
            fast = fast.next
            slow = slow.next
        #removing the next node from slow
        slow.next = slow.next.next
        return dummy.next