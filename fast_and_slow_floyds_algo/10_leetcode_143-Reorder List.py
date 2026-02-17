'''
Docstring for 10_leetcode_143-Reorder List
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
from typing import  Optional
#Singly LinkedList
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head  and not head.next:
            return None
        #to shuffle first finding the middle using floyds algo
        slow = head 
        fast = head
        #until fast reaches end - fast moving 2 steps and slow pointer moving one step- as fast reaches end slow will be at mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #now reversing the other half 
        prev = None #considering another pointer
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #merging two halves
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2