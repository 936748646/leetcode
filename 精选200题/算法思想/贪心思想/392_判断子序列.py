class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        j = 0
        for i in t:
            if s[j] == i: 
                if j < len(s) - 1: j += 1
                else: return True
        return False
