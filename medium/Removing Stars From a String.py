class Solution:
    def removeStars(self, s: str) -> str:
        letters = []
        for char in s:
            if char == "*":
                letters.pop()
            else:
                letters.append(char)

        return "".join(letters)


sol = Solution()
s = "leet**cod*e"

print(sol.removeStars(s))
