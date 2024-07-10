class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0
        for log in logs:
            if log == "../":
                if count > 0:
                    count -= 1
            elif "." != log[0]:
                count += 1

        return count if count >= 0 else 0
