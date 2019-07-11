# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        out = l3 = ListNode(0)
        while l1 or l2 :
            val = res
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next    
            res = val // 10
            val = val % 10
            l3.next = ListNode(val)
            l3 = l3.next
        if res > 0:
            l3.next = ListNode(res)
        return out.next
