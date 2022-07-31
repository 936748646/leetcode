import queue

class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()  # 使用put和get
        self.deque = queue.deque()  # collections.deque，使用append和popleft


    def max_value(self) -> int:
        # 另使用一个双向队列deque保存递减值，使得队首永远是当前队列最大值：
        # 如果入队的元素比已有的某些元素大，则【删除所有】比它小的
        # 如果出队的元素正好是最大值，这个递减队列也要删除队首元素
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)


    def pop_front(self) -> int:
        if self.queue.empty(): return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
        return val



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
