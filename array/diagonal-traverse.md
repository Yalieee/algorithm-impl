# Concept
參考[此處](http://www.cnblogs.com/grandyang/p/6414461.html)解法1

往右上走時做 (-1, +1)，而往左下走時做 (+1, -1)。當超出邊界時進行修正，要注意超出邊界時需做額外的修正。

```py
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return []

        m = len(matrix)

        if m == 0:
            return []

        n = len(matrix[0])
        result = []
        goRight = True
        left = 0
        right = 0

        for i in range(m*n):
            result.append(matrix[left][right])

            if goRight:
                left -= 1
                right += 1
            else:
                left +=1
                right -= 1

            if left > m-1:
                left = m-1
                right += 2
                goRight = True
            if right > n-1:
                right = n-1
                left += 2
                goRight = False

            if left < 0:
                left = 0
                goRight = False
            elif right < 0:
                right = 0
                goRight = True

        return result
```
