class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分法
        n = len(letters) - 1
        l, r = 0, n
        while(l <= r):
            m = l + (r - l) // 2
            if target < letters[m]: r = m - 1
            elif target >= letters[m]: l = m + 1
        return letters[l] if l <= n else letters[0]  #正常情况下最后正好是r比target小，l比target大；如果l超长度了，就说明没找到
