class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        left, right = 0, 0
        result = set()
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
                continue
            elif nums1[left] > nums2[right]:
                right += 1
                continue

            if nums1[left] == nums2[right]:
                result.add(nums1[left])

            left += 1
            right += 1

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(Solution().intersection(nums1, nums2))
