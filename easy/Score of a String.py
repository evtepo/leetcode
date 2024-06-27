class Solution:
    def scoreOfString(self, s: str) -> int:
        left, right, score = 0, len(s) - 1, 0
        while left < right:
            if left == right - 1:
                score += abs(ord(s[left]) - ord(s[right]))
                break

            score += (abs(ord(s[left]) - ord(s[left + 1])) + abs(ord(s[right]) - ord(s[right - 1])))

            left += 1
            right -= 1

        return score


s = Solution()

print(s.scoreOfString("hello"))
