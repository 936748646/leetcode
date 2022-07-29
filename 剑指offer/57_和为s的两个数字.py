class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 0
        for i in range(len(nums) - 1, -1, -1):  # 我先确定了右指针位置，可以不用
            if nums[i] < target: 
                r = i
                break
        # 头尾双指针，相加大于target，右指针左移；小于target，左指针右移
        while l != r:
            if nums[l] + nums[r] == target:
                return nums[l], nums[r]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return []
