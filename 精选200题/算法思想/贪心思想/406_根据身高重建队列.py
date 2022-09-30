class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 一般数对涉及排序的，根据第一个元素正向排序+第二个元素反向排序，或根据第一个元素反向排序+第二个元素正向排序，往往能简化解题过程
        # 先按h降序排序，再按k升序排序（贪心：h越大越应该在前面出现；k越大越应该在后面出现）
        # 然后再根据是否满足k的条件进行插入
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            if len(res) <= p[1]: res.append(p)
            else: res.insert(p[1], p)  # res中已有的元素个数已不满足p[1]要求，因此将p插入到res[p[1]]位置
        return res
