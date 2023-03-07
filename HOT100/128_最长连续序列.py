class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)  # 去重，建立set。Python的set就是hash table，因此查找时间复杂度是O(1)
        curlen, maxlen = 0, 0
        for i in nums:
            if i-1 not in hashset:  # 若x-1没在set内，证明x是一个序列的头，依次+1看是否在set中，得到该序列长度；若x-1在set内，证明x不是序列头，跳过
                curnum = i
                curlen = 1
                while curnum+1 in hashset:
                    curlen += 1
                    curnum += 1
                maxlen = max(maxlen, curlen)       
        return maxlen
