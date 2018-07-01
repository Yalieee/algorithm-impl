# Concept
先走一次算出每個數字的頻率，接下來要取得最大的 K 個。明顯是使用 Max heap 來處理比較簡單。

Python 內建的 heapq 是 Min Heap，因此把輸入進去的數值乘上 `-1` 使之實質上變成 Max heap

```py
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # generate hash map
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        heap = []
        for key, val in hashMap.iteritems():
            heapq.heappush(heap, (val * -1, key))

        output = []
        for i in range(k):
            _, key = heapq.heappop(heap)
            output.append(key)

        return output
```
