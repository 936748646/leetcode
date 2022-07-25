class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 分别两次二分搜索出现target的左右边界
        # 在二分搜索的基础上，需注意nums[m]=target时的处理：
        # m为中间点，nums[m]=target时，右边界在[m+1,j]中，左边界在[i,m-1]中
        # 因此，查找右边界：i=m+1；查找左边界：j=m-1

        # 先右边界：执行完后j为最后一个target，i为j+1（右边界）
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若j不等于target，则数组中无target
        if j >= 0 and nums[j] != target: return 0
        # 左边界
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1
