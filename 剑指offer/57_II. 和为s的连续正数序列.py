class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口，从[1,2]开始。总和小了右边界朝右，总和大了左边界朝右
        l, r, s, res = 1, 2, 3, []
        while l < r:
            if s == target:
                res.append(list(range(l, r + 1)))
                s -= l
                l += 1
            elif s < target:
                r += 1
                s += r  # r滑了s才能加r！
            else:
                s -= l
                l += 1
        return res
