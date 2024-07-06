class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        back = False
        count = 1
        for _ in range(time):
            if count == n:
                back = True
            elif back and count == 1:
                back = False

            if not back:
                count += 1
            else:
                count -= 1

        return count



print(Solution().passThePillow(4, 5)) # 2
print(Solution().passThePillow(3, 2)) # 3
print(Solution().passThePillow(9, 4)) # 5
print(Solution().passThePillow(18, 38)) # 5
