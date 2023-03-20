class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)  # 当前滑动窗口中还需要的各个字符数
                       # 窗口中包含哪个字符，哪个字符的值就-1；全为负时，代表滑动窗口满足条件
        for i in t:
            need[i] += 1
        needcount = len(t)  # 目前所需元素的总数量（记录这个是为了避免每次都去遍历need判断是否已经满足条件） 
        left = 0  # 窗口左边界
        res = [0, float('inf')]  # 记录子串起始位置
        for i, c in enumerate(s):  # 先往右增加窗口，直到包含所有所需字符
            if need[c] > 0:
                needcount -= 1
            need[c] -= 1
            if needcount == 0:  # 包含所有所需字符后，左边界右移，排出多余元素
                while True:
                    c = s[left]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    left += 1
                if i - left < res[1] - res[0]:
                    res = [left, i]
                need[s[left]] += 1  # 窗口左边界右移一个元素，开始寻找新的符合条件的滑动窗口
                needcount += 1
                left += 1
        return s[res[0]: res[1] + 1] if res[1] < len(s) else ''
