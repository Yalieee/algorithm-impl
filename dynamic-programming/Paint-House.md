# Concept
公式如下，其中 i 是第 i 個房子， j 是使用 j 號顏色
```
minCost[i][j] = cost[i][j] + min(minCost[i-1][(j+1) % 3], minCost[i-1][(j+2) % 3])
```

# Notice
這邊要注意的是，Python 沒辦法直接建立二維陣列，因此需要用 loop 初始化，並且使用 insert() 來寫入

```py
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0

        length = len(costs)
        if length == 0:
            return 0

        minCost = []
        for i in range(length):
            minCost.append([])
        minCost[0].append(costs[0][0])
        minCost[0].append(costs[0][1])
        minCost[0].append(costs[0][2])

        for number in range(1, length):
            for color in range(3):
                minCost[number].insert(
                    color,
                    costs[number][color] + min(
                        minCost[number-1][(color+1) % 3],
                        minCost[number-1][(color+2) % 3]
                    )
                )

        return min(
            minCost[length-1][0],
            minCost[length-1][1],
            minCost[length-1][2],
        )
```