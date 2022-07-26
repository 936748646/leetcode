class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1  # 只要nums[m]==m，缺失的数就在右边
            # nums[m]!=m，缺失的数就在左边
            else: j = m - 1
        return i
