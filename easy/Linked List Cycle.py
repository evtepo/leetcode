# Definition for singly-linked list.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def hasCycle(self) -> bool:
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

    def set_node(self, node: ListNode) -> None:
        if not self.head:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def get_node(self) -> list:
        lst = []
        current = self.head
        while current:
            lst.append(current.val)
            current = current.next

        return lst
    

s = Solution()

node = ListNode(7)

s.set_node(ListNode(1))
s.set_node(ListNode(2))
s.set_node(node)
s.set_node(ListNode(4))
s.set_node(ListNode(6))
s.set_node(node)

# print(s.get_node())

print(s.hasCycle())
