class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 想象成表格，分成上三角和下三角计算
        b = [1] * len(a)
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角，正向遍历a，得到b的左半边b1[i]=a[0]*...*a[i-1]
        # 上三角，逆向遍历a，得到b的右半边b2[i]=a[i+1]*...a[-1]
        # 然后左右两边相乘
        tmp = 1
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b
