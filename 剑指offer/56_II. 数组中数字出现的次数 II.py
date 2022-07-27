class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 统计所有数字各二进制位中出现1的次数，分别对3求余，每一位的求余结果放一起则为只出现一次的数
        counts = [0] * 32  # 长度32，装无符号整数各32位出现1的次数
        for num in nums:
            for i in range(32):
                counts[i] += num & 1  # and1：取num的个位
                num >>= 1  # num右移一位
        res = 0
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % 3  # 注意counts是反着存的
        return res

#  【该题修改除数3，即可解决“除一个数字只出现一次外，其他数字都出现*次”的问题】
