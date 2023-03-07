# 思路：使用一个双向链表+一个hash table来实现
# 1. 双向链表模拟使用记录顺序，最近使用的放链表头，最久使用的放链表尾
# 2. hash table模拟缓存存储：{key: node}

class DoubleLinkedNode:  # 双向链表
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 定义伪头部、伪尾部，方便判断链表头尾
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0  # 记录目前已有元素个数


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 若key存在，则在记录链表中移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            self.size += 1
            if self.size > self.capacity:
                node_old = self.removeTail()
                self.cache.pop(node_old.key)
                self.size -= 1
            node_new = DoubleLinkedNode(key, value)
            self.cache[key] = node_new
            self.addToHead(node_new)


    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
