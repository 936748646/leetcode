class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表{num:i}，直接通过key=target-num找符合的数的位置i
        h = dict()
        for i, num in enumerate(nums):
            if target - num in h:
                return [h[target - num], i]
            h[num] = i 
        return []
