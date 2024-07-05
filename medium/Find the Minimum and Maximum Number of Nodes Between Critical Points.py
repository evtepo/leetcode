# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        current, prev = head.next, head
        points = []
        count = 1
        while current and current.next is not None:
            if prev.val < current.val > current.next.val or prev.val > current.val < current.next.val:
                points.append(count)

            count += 1
            current = current.next
            prev = prev.next

        if len(points) < 2:
            return [-1, -1]

        mx = points[-1] - points[0]
        mn = float("inf")

        for i in range(1, len(points)):
            mn = min(mn, points[i] - points[i - 1])

        return [mn, mx]
