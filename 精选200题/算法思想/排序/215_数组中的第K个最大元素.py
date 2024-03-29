class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速选择（堆方法见【初、中级算法】文件夹）
        def partition(nums, left, right):
            i, j, pivot = left, right, nums[left]
            while i < j:
                while i < j and nums[j] >= pivot: j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot: i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            return i
        def topk_split(nums, k, left, right):
            if left < right:
                index = partition(nums, left, right)
                if index == k: return
                elif index < k: topk_split(nums, k, index+1, right)
                else: topk_split(nums, k, left, index - 1)
        topk_split(nums, len(nums) - k, 0, len(nums) - 1)
        return nums[len(nums) - k]
