class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return nums[i] + 1
    

print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
        