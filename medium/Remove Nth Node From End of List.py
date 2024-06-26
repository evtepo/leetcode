# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(next=head)
        top = fake
        count = 0
        while head:
            count += 1
            head = head.next

        node_number = count - n
        for _ in range(node_number):
            fake = fake.next

        fake.next = fake.next.next

        return top.next
