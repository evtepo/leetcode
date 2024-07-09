class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        if not score:
            return result

        score_dict = {}
        places = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }
        for i, v in enumerate(sorted(score, reverse=True)):
            if val := places.get(i + 1):
                score_dict[v] = val
            else:
                score_dict[v] = str(i + 1)

        for value in score:
            result.append(score_dict[value])

        return result


print(Solution().findRelativeRanks(score=[10, 3, 8, 9, 4]))
