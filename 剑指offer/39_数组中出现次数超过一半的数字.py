class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x
