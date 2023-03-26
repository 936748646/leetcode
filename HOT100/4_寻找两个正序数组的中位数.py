class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        l = len(nums1)
        return nums1[l // 2] if l % 2 else (nums1[l // 2 - 1] + nums1[l // 2]) / 2
