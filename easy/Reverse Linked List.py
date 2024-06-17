# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nodes = [node for node in self.get_node()]
        top = self.head
        self.head = None
        for node in nodes[::-1]:
            self.set_node(node)

        top.next = None

    def set_node(self, node: ListNode):
        if not self.head:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

    def get_node(self):
        current = self.head
        while current:
            yield current
            current = current.next


s = Solution()

s.set_node(ListNode(1))
s.set_node(ListNode(4))
s.set_node(ListNode(5))
s.set_node(ListNode(7))

lst = [node for node in s.get_node()]

s.reverseList(ListNode())

reversed_lst = [node for node in s.get_node()]
