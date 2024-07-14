class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        left = nums[len(nums) // 2]
        if len(nums) % 2 == 0:
            left = nums[len(nums) // 2 - 1]
            right = nums[len(nums) // 2]

            return float((left + right) / 2)
        
        return float(left)
