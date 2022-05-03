#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.list = nums

    def reset(self) -> List[int]:
        return self.list

    def shuffle(self) -> List[int]:
        list_copy = self.list[:]
        for j in range(1, len(list_copy)):
            i = random.randint(0, j)
            self.swap(list_copy, i, j)
        return list_copy

    def swap(self, list, i ,j):
        if i != j:
            list[i] = list[i] + list[j]
            list[j] = list[i] - list[j]
            list[i] = list[i] - list[j]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

