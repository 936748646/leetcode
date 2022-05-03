#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (countMost - 1) * n + countMost + maxCount - 1
        # countMost: 频率最高任务出现的次数; maxCount: 频率最高任务的个数
        if n == 0:
            return len(tasks)
        collection = Counter(tasks)
        sorted_list = sorted(collection.items(), key=lambda x: x[1], reverse=True)
        task, countMost = sorted_list.pop(0)
        maxCount = 1
        for task, count in sorted_list:
            if count == countMost:
                maxCount += 1
            else:
                break
        res = (countMost - 1) * n + countMost + maxCount - 1
        return max(res, len(tasks))
# @lc code=end

