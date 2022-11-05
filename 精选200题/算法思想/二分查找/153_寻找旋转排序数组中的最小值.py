class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] <= nums[h]: h = m  # m位置小于h位置，说明在左边
            else: l = m + 1  # 大于，则最小值必定在m右边
        return nums[l]
