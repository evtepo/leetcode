class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        result = 0
        one_letter = 0
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        for value in letters.values():
            if value % 2 != 0:
                result += value - 1
                one_letter = 1
            else:
                result += value

        return result + one_letter
