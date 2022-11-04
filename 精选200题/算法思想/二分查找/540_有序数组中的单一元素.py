class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 规律：nums[偶]==nums[奇]->单个的数在后面；nums[偶]!=nums[奇]->单个的数在前面
        l, h = 0, len(nums) - 1
        while l < h:  # 循环条件只能<，不能<=。因为使用了h=m，循环可能会无法退出
            m = l + (h - l) // 2
            if m % 2 == 1: m -= 1 # 如果是奇数就回退一个，就是偶数了
            if nums[m] == nums[m + 1]: l = m + 2
            else: h = m
        return nums[l]
