#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return []
        d = dict()
        res = []
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        d_ordered_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for d_key in d_ordered_list:
            if k > 0:
                res.append(d_key[0])
                k -= 1
            else:
                break
        return res
# @lc code=end

