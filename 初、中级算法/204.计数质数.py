#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃式筛选法：一个素数的各个倍数，是一个差为此素数本身的等差数列
        if n == 0 or n == 1:
            return 0
        isPrimes = [True] * n
        i = 2
        while i * i < n:
            if isPrimes[i]:
                x = i
                while i * x < n:
                    isPrimes[i * x] = False
                    x += 1
            i += 1
        count = 0
        for i in range(2, n):
            if isPrimes[i]:
                count += 1
        return count
# @lc code=end

