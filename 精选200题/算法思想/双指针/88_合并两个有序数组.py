class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, index = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            # if p1 < 0:
            if p1 < 0 or nums1[p1] <= nums2[p2]: 
                nums1[index] = nums2[p2]
                index -= 1
                p2 -= 1
            # elif nums1[p1] > nums2[p2]: 
            else:
                nums1[p1], nums1[index] = nums1[index], nums1[p1]
                index -= 1
                p1 -= 1
            '''
            # 与第一个if情况合并了
            else: 
                nums1[index] = nums2[p2]
                index -= 1
                p2 -= 1
            '''
'''
两数组指针从后往前（m->0，n->0），更大的数与index交换
判断结束标志为nums2全被插入
这里注意一个特殊情况是p1（也就是nums1有数字的部分）已经被比较完，p1<0，nums1前面全是0的时候（nums[0]~nums[index]都为0）
只需要逐个将nums2剩下的数放到nums1前面的0的位置来即可
'''
