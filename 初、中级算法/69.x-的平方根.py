#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            res = mid * mid
            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            else:
                temp = (mid + 1) * (mid + 1)
                if temp > x:
                    return mid
                left = mid + 1
        return -1
# @lc code=end

