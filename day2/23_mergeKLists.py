# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = []
        for li in lists:
            while li:
                lst.append(li)
                li = li.next
        lst.sort(key=lambda x: x.val)
        res = ListNode(0)
        r = res
        for li in lst:
            r.next = li
            r = r.next
        return res.next
