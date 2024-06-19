# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        fake = ListNode(0)
        top = fake
        current = head
        while current:
            if current.val == val:
                current = current.next
                if not current:
                    fake.next = current
            else:
                fake.next = current
                fake = fake.next
                current = current.next

        return top.next


[1,2,6,3,4,5,6]

n7 = ListNode(6)
n6 = ListNode(5, n7)
n5 = ListNode(4, n6)
n4 = ListNode(3, n5)
n3 = ListNode(6, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)


s = Solution()

print(s.removeElements(n1, 6))
