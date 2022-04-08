class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        # 使用列表记录已出现过的数字
        dic = []
        for n in nums:
            if n in dic:
                return n
            else:
                dic.append(n)
