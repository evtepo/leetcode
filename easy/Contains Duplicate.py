class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        res = None
        count = 0
        for num in nums:
            if res is None:
                res = num
                count += 1
                continue

            if res == num:
                return True

            res = num

        return False
