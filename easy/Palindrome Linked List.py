# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        nodes_val = []
        while head:
            nodes_val.append(head.val)
            head = head.next

        left = 0
        right = len(nodes_val) - 1
        while left < len(nodes_val):
            if nodes_val[left] != nodes_val[right]:
                return False
            
            left += 1
            right -= 1

        return True



node4 = ListNode(1)
node3 = ListNode(1, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

s = Solution()

print(s.isPalindrome(node1))
