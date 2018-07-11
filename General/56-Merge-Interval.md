# Concept
在合併的時候，有可能一開始看不出可以合併，要跟後面的元素一起才能串起來。因此如果先用第一個元素排序的話，就可以照順序產生出結果。

藉由比較結果的 end 和之後每個的 start，來看是否會產生一串新的 interval。如果不是新的 interval，就用 max來更新最大值

```py
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not result or result[-1].end < interval.start:
                result.append(interval)
            elif result[-1].end >= interval.start:
                result[-1].end = max(result[-1].end, interval.end)

        return result
```