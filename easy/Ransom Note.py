class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for char in magazine:
            letters[char] = letters.get(char, 0) + 1

        for char in ransomNote:
            letters[char] = letters.get(char, 0) - 1
            if letters[char] < 0:
                return False

        return True
