# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        out = l = ListNode(0)
        nodelist = []
        while head:
            nodelist.append(head)
            head = head.next
            if len(nodelist) == k:
                nodelist.reverse()
                for node in nodelist:
                    l.next = node
                    l = l.next
                nodelist = []
                l.next =None
        if nodelist:
            l.next = nodelist[0]
        return out.next
