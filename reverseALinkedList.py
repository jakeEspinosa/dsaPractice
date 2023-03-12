'''
Reverse a Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n)

Space Complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous