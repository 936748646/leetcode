class Solution:
    # dp[i][j]代表s的前i个字符是否和p的前j个字符匹配，即s[0,i-1]和p[0,j-1]是否匹配
    # 太难了搞不懂
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False for i in range(n)] for j in range(m)]
        dp[0][0] = True  # 两个空字符串可以匹配
        # 初始化首行，i=0时s为空，p只能偶数位为'*'才能匹配
        for j in range(2, n, 2):  # 步长为2          
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if (dp[i][j - 2] 
                    or (dp[i - 1][j] and s[i - 1] == p[j - 2]) 
                    or (dp[i - 1][j] and p[j - 2] == '.')):
                        dp[i][j] = True
                else:
                    if ((dp[i - 1][j - 1] and s[i - 1] == p[j - 1])
                    or (dp[i - 1][j - 1] and p[j - 1] == '.')):
                        dp[i][j] = True
        return dp[-1][-1]
