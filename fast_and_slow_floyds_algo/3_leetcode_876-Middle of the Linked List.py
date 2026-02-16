'''
Docstring for 3_leetcode_876-Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
from typing import Optional
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using floyd's algo of slow and fast two pointers pattern
        fast = head
        slow = head
        # to find the middle element move slow pointer one step and 
        # fast two step when the fast reaches end tht is mid return that element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    #Time Complexity = O(n) Space Compelxity = O(1)