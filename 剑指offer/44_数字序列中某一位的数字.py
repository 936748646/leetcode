class Solution:
    def findNthDigit(self, n: int) -> int:
        # 方法：把整个字符序列按位数划分（1~9、10~99、100~999...）
        # 1.先确定n所在数字的位数区间（一位数、两位数还是三位数...）
        # 2.再确定n所在的数字（例如两位数区间，是10、11还是12...）
        # 3.最后确定n是数字中哪一位（例如n在12里，是第一位1，还是第二位2）
        # n：位数；num：数字；digit：数字的位数；
        # start：每digit位数范围数字的起始数字（例如两位数范围起始数字start=10）
        # 每位数范围包含的数字数量：9*start；包含的数位总数：count=9*start*digit
        digit, start, count = 1, 1, 9
        while n > count:  # n循环减去每组位数count，直到n＜=count为止
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        s = str(num)
        res = int(s[(n - 1) % digit])  # 3.
        return res
