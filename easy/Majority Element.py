class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        digits = {}
        for num in nums:
            digits[num] = digits.get(num, 0) + 1

        for key, value in digits.items():
            if value >= len(nums) / 2:
                return key


nums = [6,5,5]

print(Solution().majorityElement(nums))
