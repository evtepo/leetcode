class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1, s2 = list(s1), list(s2)

        s1[0], s1[2] = s1[2], s1[0]
        if s1 == s2:
            return True
        
        s1[1], s1[3] = s1[3], s1[1]
        if s1 == s2:
            return True
        
        s1[0], s1[2] = s1[2], s1[0]
        return s1 == s2

        
        

s = Solution()

print(s.canBeEqual(s1 = "bnxw", s2 = "bwxn"))
