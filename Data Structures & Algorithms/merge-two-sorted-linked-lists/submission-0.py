# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        merge_list = dummy
        curr_list1 = list1
        curr_list2 = list2
        while curr_list1 and curr_list2:
            if curr_list1.val <= curr_list2.val:
                merge_list.next = curr_list1
                curr_list1 = curr_list1.next
            else:
                merge_list.next = curr_list2
                curr_list2 = curr_list2.next
            merge_list = merge_list.next
        merge_list.next = curr_list1 if curr_list1 else curr_list2
        return dummy.next