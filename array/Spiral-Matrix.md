# Concept
四個步驟照順序走，當走完一個步驟時就縮小範圍，最後會剩下一排直的或是一排橫的，再對這兩種情況特別處理即可。要注意限縮範圍後可能會影響後面兩步，要做好檢查。


```py
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        result = []
        leftBound = 0
        rightBound = n-1
        upBound = 0
        lowerBound = m-1

        while leftBound <= rightBound and upBound <= lowerBound:
            if leftBound == rightBound:
                for i in range(upBound, lowerBound+1):
                    result.append(matrix[i][leftBound])
                break
            elif upBound == lowerBound:
                for i in range(leftBound, rightBound+1):
                    result.append(matrix[upBound][i])
                break

            # go right
            for i in range(leftBound, rightBound+1):
                result.append(matrix[upBound][i])

            upBound += 1

            # go down
            for i in range(upBound, lowerBound+1):
                result.append(matrix[i][rightBound])

            rightBound -= 1

            # go left
            if leftBound < rightBound:
                for i in range(rightBound, leftBound-1, -1):
                    result.append(matrix[lowerBound][i])

                lowerBound -= 1

            # go up
            if upBound < lowerBound:
                for i in range(lowerBound, upBound-1, -1):
                    result.append(matrix[i][leftBound])

                leftBound +=1

        return result
```