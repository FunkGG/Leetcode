# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        out = ListNode(0)
        if not head:
            return None
        if not head.next:
            return head
        l1 = head
        i = 1
        while k:
            i += 1
            l1 = l1.next
            if not l1:
                l1 = head
                k = k%(i-1)-1
            else:
                k -= 1
        l2 = head
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        l1.next = head
        out.next = l2.next
        l2.next =None
        return out.next
