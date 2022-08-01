class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 条件转化为：1. 5张牌无重复；2. max-min＜5
        repeat = set()
        max_val, min_val = 0, 13
        for num in nums:
            if num == 0: continue
            max_val = max(max_val, num)
            min_val = min(min_val, num)
            if num in repeat: return False
            repeat.add(num)
        return max_val - min_val < 5
