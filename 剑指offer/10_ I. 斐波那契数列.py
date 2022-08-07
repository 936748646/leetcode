class Solution:
    # 递归超时
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            nums = [0, 1]
            for i in range(2, n + 1):
                nums.append((nums[i - 1] + nums[i - 2]) % 1000000007)
            return nums.pop()
