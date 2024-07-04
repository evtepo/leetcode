# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        current = head
        while current.next:
            if current.next.val == 0:
                last = current
                current = current.next

            if current.next:
                current.val += current.next.val
                current.next = current.next.next

        last.next = None

        return head
    
node8 = ListNode(0)
node7 = ListNode(2, node8)
node6 = ListNode(5, node7)
node5 = ListNode(4, node6)
node4 = ListNode(0, node5)
node3 = ListNode(1, node4)
node2 = ListNode(3, node3)
node1 = ListNode(0, node2)

print(Solution().mergeNodes(node1))
