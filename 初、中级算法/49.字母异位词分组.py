#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = dict()
        for s in strs:
            temp = list(s)
            temp.sort()
            key = ''.join(temp)
            if key in dic.keys():
                dic[key].append(s)
            else:
                dic[key] = [s]
        for i in dic.values():
            res.append(i)
        return res
# @lc code=end

