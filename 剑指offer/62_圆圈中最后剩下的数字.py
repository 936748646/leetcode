class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # n约瑟夫环问题，递推公式表示索引。太难理解了，直接写公式结果
        # f(n,m)=[f(n-1,m)+m]%n,n>1;0,n=1
        x = 0  # n=1
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
