# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        while(l < h):
            m = l + (h - l) // 2
            if isBadVersion(m): h = m
            else: l = m + 1
        return l
