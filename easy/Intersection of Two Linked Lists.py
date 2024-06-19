# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        nodes = {}
        while headA:
            nodes[headA] = "t"
            headA = headA.next

        while headB:
            if headB in nodes.keys():
                return headB

            headB = headB.next

        return None

