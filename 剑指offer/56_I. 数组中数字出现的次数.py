class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 如果数组中只有一个数字出现一次，则所有数字异或的结果即为该数
        # 然而该数组有两个数字x、y出现一次，因此将数组拆分成两个子数组分别异或
        # 拆分方法：这两个数字二进制位至少有一位不同，因此这两个数字的异或结果至少有一位是1
        # 找到这一位，从这一位的不同来分组
        x, y, n, m = 0, 0, 0, 1
        for num in nums:
            n ^= num  # n为x、y的异或结果
        while n & m == 0:  # 将n的每一位与1（m）进行and，结果为1则找到了这一位
            m <<= 1  # m左移一位
        for num in nums:  # 分为这一位为1和这一位为0的两组
            if num & m: x ^= num
            else: y ^= num
        return x, y56_
