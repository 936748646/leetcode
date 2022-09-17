class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 桶排序（直接使用dict的value排序的方法见初、中级算法）
        freq = {}  # dict记录数字出现频率
        for i in nums:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        bucket = [None] * (len(nums) + 1)  # 桶序号代表频率，每个桶保存相同频率的数组成的列表
        for i in freq.keys():
            if not bucket[freq[i]]: 
                bucket[freq[i]] = []
            bucket[freq[i]].append(i)
        ans = []
        for i in range(len(bucket) - 1, -1, -1):  # 从后往前输出k个数
            if not bucket[i]: continue
            ans.extend(bucket[i])
            if len(ans) == k: return ans
        return ans
