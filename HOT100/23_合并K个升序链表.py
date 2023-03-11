# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 直接用heapq库的小顶堆
        heap = []
        head = ListNode()
        res = head
        for i in range(len(lists)):
            while lists[i]:
                heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        for i in range(len(heap)):
            head.next = ListNode(heappop(heap))
            head = head.next
        return res.next

# 以上是直接全部node一起放入小顶堆再一个个弹出的方法，但是这样和乱序链表合并没区别
# 更优做法是利用所给链表有序的条件：先放入每个list的第一个元素（[1,1,2]），pop最小的node当res头；
# 然后每次再放一个node进来，pop，再放，再pop...保证堆里包含了当前最小的node
# 虽然更省时，但我不想写了
