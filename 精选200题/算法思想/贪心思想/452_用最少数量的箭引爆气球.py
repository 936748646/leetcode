class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 相当于找不重叠区间(435)
        points = sorted(points, key = lambda kv: kv[1])
        end = points[0][1]
        cnt = 1
        for i in range(1, len(points)):
            if points[i][0] <= end: continue
            end = points[i][1]
            cnt += 1
        return cnt
