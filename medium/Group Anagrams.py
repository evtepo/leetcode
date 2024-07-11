class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if not result.get(sorted_s):
                result[sorted_s] = []

            result[sorted_s].append(s)

        return list(result.values())
        
    

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
