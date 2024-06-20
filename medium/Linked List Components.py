# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        count = 0
        flag = False
        while head:
            if head.val in nums:
                flag = True
            elif flag:
                flag = False
                count += 1

            head = head.next

        if flag:
            count += 1

        return count


[0, 1, 2, 3]  # ListNode
[0, 1, 3]  # nums
