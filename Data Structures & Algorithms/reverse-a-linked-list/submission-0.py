# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        reverse = None
        while node:
            nxt = node.next
            node.next = reverse
            reverse = node
            node = nxt
        return reverse