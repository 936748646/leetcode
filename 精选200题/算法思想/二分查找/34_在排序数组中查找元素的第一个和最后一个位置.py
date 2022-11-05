class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 需要写两次二分查找分别找前和后两个位置
        # 可以转换为只写查找起始位置的函数：找一次target的起始位置，再找一次target+1的起始位置回退一位作为target的结束位置
        def findFirst(nums, target):
            l, h = 0, len(nums)  # h取len(nums)原因：target大于nums最后一个元素时，查找范围没有囊括到，因此要扩大一个才能找到。
                                 # 我们其实希望findFirst输出target的真实位置，即nums最后位再往后一位（也就是len(nums)位置）。
                                 # 例子：[2,2],2
            while l < h:
                m = l + (h - l) // 2
                if nums[m] >= target: h = m
                else: l = m + 1
            return l
        start, end = findFirst(nums, target), findFirst(nums, target + 1) - 1
        return [-1, -1] if start == len(nums) or nums[start] != target else [start, max(start, end)]  
        # 最后一个max用于避免只有一个数，start为0，end会为-1的情况；
        # 前面一个start == len(nums)用于没找到target且start越界了的情况
