# Concept
每一行的頭尾都是 1，只差在中間。中間的數目可以從層數推出來，數字則是前一行的 n-1 + n。

```py
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        result = [[1]]
        for level in range(1, numRows):
            row = []
            # first element
            row.append(1)

            startIndex = 1
            for i in range(level-1):
                row.append(result[level-1][startIndex-1] + result[level-1][startIndex])
                startIndex += 1

            # last element
            row.append(1)

            result.append(row)

        return result
```
