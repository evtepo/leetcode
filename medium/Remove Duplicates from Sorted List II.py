# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def __init__(self) -> None:
        self.head = None

    def deleteDuplicates(self) -> ListNode:
        top = ListNode(0)
        top.next = self.head
        current = self.head
        prev = top
        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = prev.next

        self.head = top.next

    def set_node(self, value):
        if not self.head:
            self.head = ListNode(value)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = ListNode(value)

    def get_nodes(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next

        return nodes
