class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = None
        count = 0
        nums.sort()
        for num in nums:
            if res is None:
                res = num
                count += 1
                continue

            if num == res:
                count -= 1

            if num != res and count <= 0:
                count = 1
                res = num

        return res


nums = [1,0,1]

print(Solution().singleNumber(nums))
