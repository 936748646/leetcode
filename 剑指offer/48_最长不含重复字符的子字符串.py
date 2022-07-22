class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 设s[j]左边距离最近的相同字符为s[i]
        # 1.i<0: dp[j]=dp[j-1]+1
        # 2.dp[j-1]<j-i: 说明i在dp[j-1]所计算的区间之外，不用考虑。dp[j]=dp[j-1]+1
        # 3.dp[j-1]>=j-i: 说明i在dp[j-1]所计算的区间之内，dp[j]要重新从i开始计算。dp[j]=j-i
        # 如何获得i：在遍历s的同时，存储每个字符最后一次出现的位置
        # 遍历到s[j]时，访问dic[s[j]]获得i
        dic = {}
        res = tmp = 0  # tmp：dp[j-1]
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j  # 更新s[j]的索引
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res
