# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeList=[]
        while head:
            nodeList.append(head)
            head = head.next
        if n < len(nodeList):
            nodeList[-n-1].next = nodeList[-n].next
            return nodeList[0]
        else:
            return nodeList[0].next
