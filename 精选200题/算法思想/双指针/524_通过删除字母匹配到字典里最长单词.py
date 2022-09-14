class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubstr(long, short):
            i, j = 0, 0
            while i < len(long) and j < len(short):
                if long[i] == short[j]: j += 1
                i += 1
            return True if j == len(short) else False
        res = ""
        for i in dictionary:
            if isSubstr(s, i):
                if len(i) > len(res) or (len(i) == len(res) and res > i): res = i
        return res
