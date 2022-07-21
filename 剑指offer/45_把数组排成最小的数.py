class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 'x'+'y' >= 'y'+'x'可得x“大于”y
        # 按照这个“大于”“小于”来从小到大排序数组
        # 方法：修改快排中的大小判断条件
        def quick_sort(l, r):  # 快排s[l]~s[r]，以s[l]为基准
            if l >= r:
                return
            i, j = l, r  # 从两头分别开始
            while i < j:
                # 找到比基准值小的strs[j]
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                # 找到比基准值大的strs[i]
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]  # 交换
            strs[i], strs[l] = strs[l], strs[i]  # 基准值更新为小的
            # 以i为界，分别快排两部分
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)
        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)
