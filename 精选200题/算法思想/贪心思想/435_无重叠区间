class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按区间尾大小来排序，优先选择不重叠且区间尾小的，以保证不重叠区间数最多
        # 问题转化为找最多的不重叠区间数，返回总区间数-不重叠区间数即可
        intervals = sorted(intervals, key = lambda kv: kv[1])
        cnt = 1  # 无重叠区间个数
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end: continue  # 重叠
            else:
                end = intervals[i][1]
                cnt += 1
        return len(intervals) - cnt
