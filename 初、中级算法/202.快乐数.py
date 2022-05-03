#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution: 
    def isHappy(self, n: int) -> bool:
        res_list = []  # 存放出现过的数
        return self.compute(n, res_list)      
        
    def compute(self, n, res_list):
        if n == 1:
            return True
        if n in res_list:
            return False
        res_list.append(n)
        str_n = str(n)
        res = 0
        for i in range(len(str_n)):
            res += int(str_n[i]) ** 2
        return self.compute(res, res_list)
# @lc code=end

