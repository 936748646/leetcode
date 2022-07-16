import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 用小顶堆存大的一半，大顶堆存小的一半
        # [am,...,a2,a1][b1,b2,...,bn]  m=n+1（N为奇数）;m=n（N为偶数）
        # am>...>a2>a1>b1>b2>...>bn
        self.A = []
        self.B = [] 


    def addNum(self, num: int) -> None:
        # 若N为奇，则num需插入B中。操作：向A插入num，再弹出A堆顶元素压入B
        # heapq.heappush：自动建立小顶堆 而大顶堆就用插入负的元素来实现
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        # 若N为偶，则num需插入A中。操作：向B插入num，再弹出B堆顶元素压入A
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))


    def findMedian(self) -> float:
        if len(self.A) != len(self.B):
            return self.A[0]
        else:
            return (self.A[0] - self.B[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
