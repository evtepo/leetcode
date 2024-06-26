class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations = []
        if not target:
            return operations

        indx = 0
        num = 1
        while indx < len(target):
            if target[indx] == num:
                operations.append("Push")
                indx += 1
                num += 1
            else:
                operations.append("Push")
                operations.append("Pop")
                num += 1

        return operations
