class Solution:
    def isHappy(self, n: int) -> bool:
        digits = set()
        while n != 1 and n not in digits:
            digits.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1


print(Solution().isHappy(n=11))
