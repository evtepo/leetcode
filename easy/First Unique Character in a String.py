class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for indx, letter in enumerate(s):
            if letter in letters:
                letters[letter] = None
            else:
                letters[letter] = indx

        for value in letters.values():
            if value is not None:
                return value

        return -1


print(Solution().firstUniqChar("leetcode"))
