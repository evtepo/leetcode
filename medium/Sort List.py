# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        sorted_nodes = self.quick_sort(nodes)
        for i in range(1, len(sorted_nodes)):
            sorted_nodes[i - 1].next = sorted_nodes[i]

        sorted_nodes[-1].next = None

        return sorted_nodes[0]

    def quick_sort(self, nodes: list[ListNode] | None):
        if not nodes:
            return []

        pivot = nodes[len(nodes) // 2]
        less, equal, greater = [], [], []

        for node in nodes:
            if node.val < pivot.val:
                less.append(node)
            elif node.val > pivot.val:
                greater.append(node)
            else:
                equal.append(node)

        return self.quick_sort(less) + equal + self.quick_sort(greater)
