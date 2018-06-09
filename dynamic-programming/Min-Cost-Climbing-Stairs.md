# Concept
題目的意思是，付出代價後就能選擇要走 1 步或是 2 步，因此列出公式如下
```
cost1 = minCost(n-1) + cost(n-1)
cost2 = minCost(n-2) + cost(n-2)
minCost(n) = min(cost1, cost2)
```


```py
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if not cost:
            return 0

        length = len(cost)
        minCost = {}

        if length == 0:
            return 0
        elif length == 1:
            return cost[0]

        minCost[0] = 0
        minCost[1] = 0

        for i in range(2, length+1):
            minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])

        return minCost[length]
```