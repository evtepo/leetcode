class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] in numbers and i - numbers[nums[i]] <= k:
                return True
            else:
                numbers[nums[i]] = i

        return False
