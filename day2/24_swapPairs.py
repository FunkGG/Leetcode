# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l1 = []
        l2 = []
        while head:
            l1.append(head)
            head = head.next
            if head:
                l2.append(head)
                head = head.next
        out = l = ListNode(0)
        if l1:
            l1[-1].next = None
        while l2:
            l2[0].next = l1[0]
            l.next = l2.pop(0)
            l = l1.pop(0)
        if l1:
            l.next = l1[0]
        return out.next    
