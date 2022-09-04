class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j] and (isPalindrome(i + 1, j) or isPalindrome(i, j - 1)):
                return True
            else: return False
        return True
# 我第一次想的方法是不写函数，直接在while里判断 if s[i+1]==s[j]，就跳过一个i（执行i+=2）；elif s[i]==s[j-1]，就跳过一个j（执行j-=2）
# 这种方法的错误是两个if分步执行，有可能先成功跳过一个i，继续发现不是回文，就直接返回false了；但如果跳过一个j，却可以是回文，这种情况没有考虑到
