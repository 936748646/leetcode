#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"       
        res = []
        s = self.countAndSay(n - 1)
        local = s[0]
        count = 0
        for i in range(len(s)):
            if s[i] == local:
                count += 1
            else:
                res.append(str(count))
                res.append(local)
                count = 1
                local = s[i]
        res.append(str(count))
        res.append(local)
        return "".join(res)
# @lc code=end

