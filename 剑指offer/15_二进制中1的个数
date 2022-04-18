class Solution:
    # 判断最右位是否为1，然后右移
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res
