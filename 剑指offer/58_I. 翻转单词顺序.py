class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        tmp = s.split()
        tmp.reverse()
        return ' '.join(tmp)
