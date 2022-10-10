class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 出现前>后，优先考虑“改前不改后”，因为把后改大，容易造成它又大于它后面的数
        # 可以拯救的情况有两种，第一种是有一对逆序，第二种是三个数逆序
        # 一对逆序：令nums[i-1]=nums[i]（4,2,3）
        # 三个数逆序：nums[i]<nums[i-2] (4,3,2)，只能令nums[i]=nums[i-1]
        cnt = 0
        for i in range(1, len(nums)):           
            if nums[i] >= nums[i - 1]: continue
            cnt += 1
            if cnt > 1: return False
            if i - 2 >= 0 and nums[i] < nums[i - 2]: nums[i] = nums[i - 1]
            else: nums[i - 1] = nums[i]
        return True
