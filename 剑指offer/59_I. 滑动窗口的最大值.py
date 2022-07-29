class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列deque，保持deque内元素递减，添加nums[j+1]时删除deque内＜nums[j+1]的数
        # 左边界从i=1-k开始，保证窗口内的数从1个开始增加到k个
        # 右边每向右添加一个数，就删掉当前窗口内小于所添加的这个数值的数，保证窗口内递减，也就是第一个数最大
        # 这样操作省去了暴力求解里重复比较窗口内已比较过的值的时间
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n - k + 1), range(n)):  
            # zip(range(),range())：同时遍历，每次循环分别获取两个的下一个元素
            if i > 0 and deque[0] == nums[i - 1]:  # 左边界右移（没删数字的情况下）
                deque.popleft()
            while deque and deque[-1] < nums[j]:  # 保持递减
                deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])  # 添加最大值（第一个数）
        return res
