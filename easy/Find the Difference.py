class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        letters = {}
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1
            letters[t[i]] = letters.get(t[i], 0) + 1

        letters[t[-1]] = letters.get(t[-1], 0) + 1

        for val in letters.values():
            if val % 2 != 0:
                return val
