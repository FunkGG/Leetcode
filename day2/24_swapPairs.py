# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        out = l1 = ListNode(0)
        while head:
            tmp = head
            head = head.next
            tmp.next = None
            if head:
                l1.next = head
                l1 = head
                head = head.next
                l1.next = tmp
                l1 = tmp
            else:
                l1.next = tmp
        return out.next
