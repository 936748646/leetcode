class Solution:
    def translateNum(self, num: int) -> int:
        # num=x[1]...x[i-2]x[i-1]x[i]，把x[i-1]x[i]拎出来，有两种情况：
        # 1.x[i-1]x[i]能整体翻译：① 整体翻译：dp[i]=dp[i-2]；② 单独翻译：dp[i]=dp[i-1]
        #                       总共dp[i]=dp[i-2]+dp[i-1]
        # 2.x[i-1]x[i]不能整体翻译：dp[i]=dp[i-1]
        # 为节省空间，只定义dp[i-1]、dp[i-2]为a、b，后面往前移
        s = str(num)
        a = b = 1  # dp[1]、dp[0]
        for i in range(2, len(s) + 1):
            tmp = s[i - 2: i]
            if "10" <= tmp <= "25":
                c = a + b
            else:
                c = a
            b = a
            a = c
        return a
