'''
Docstring for 9_gfg_Length of cycle in Linked List
Given the head of a singly linked list, determine the length of the cycle (loop) if one exists. A cycle occurs when a node's next pointer points to a previously visited node in the list. If no cycle is present, return 0.
https://www.geeksforgeeks.org/dsa/find-length-of-loop-in-linked-list/
'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def lengthOfLoop(self, head: ListNode[int]) -> int:
        length = 0
        #using floyds algo - two pointer approach
        slow = head
        fast = head
        #detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            #count cycle length
            length = 1
            temp = slow.next
            while temp != slow:
                length += 1
                temp = temp.next
            return length
        return length