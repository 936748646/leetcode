#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        self.backTrack(cur, res, 0, 0, n)
        return res
    def backTrack(self, cur, res, left, right, n):
        if len(cur) >= n * 2:
            temp = []
            for i in cur:
                temp.append(i)
            res.append(''.join(temp))
            return
        if left < n:
            cur.append('(')
            self.backTrack(cur, res, left + 1, right, n)
            del cur[-1]
        if left > right:
            cur.append(')')
            self.backTrack(cur, res, left, right + 1, n)
            del cur[-1]
# @lc code=end

