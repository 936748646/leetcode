class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexs = {}
        output = []
        for i in range(0, len(s)):
            lastIndexs[s[i]] = i
        start = 0
        while start < len(s):
            last = lastIndexs[s[start]]
            j = start + 1
            while j < last:  # 这一段我用for来写的，但是for不能改变循环变量值，导致错误
                             # for j in range(start, last) 中的last不会改变
                if lastIndexs[s[j]] > last: last = lastIndexs[s[j]]
                j += 1
            output.append(last - start + 1)
            start = last + 1
        return output
