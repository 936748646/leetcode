#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits or len(digits) == 0:
            return res
        path = []
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.backTrack(digits, path, 0, res, dict)
        return res
    def backTrack(self, digits, path, begin, res, dict):
        if len(path) == len(digits):
            temp = []
            for i in path:
                temp.append(i)
            res.append(''.join(temp))
            return
        for i in range(begin, len(digits)):
            s = dict[str(digits[i])]
            for j in range(0, len(s)):
                path.append(s[j])
                self.backTrack(digits, path, i + 1, res, dict)
                del path[-1]
# @lc code=end

