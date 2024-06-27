class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            if i >= len(s) - i:
                break

            s[i], s[len(s) - 1] = s[len(s) - 1], s[i]
