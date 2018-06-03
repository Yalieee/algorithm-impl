# Concept
搭配 carry 從右邊往左處理就好。要注意 int list 是不能直接轉成字串的，要把每個元素轉成字串類型

```py
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lastIndexA = len(a) -1
        lastIndexB = len(b) -1
        carry = 0

        result = []
        while lastIndexA >= 0 or lastIndexB >= 0:
            valA = 0
            if lastIndexA >= 0:
                valA = int(a[lastIndexA])

            valB = 0
            if lastIndexB >= 0:
                valB = int(b[lastIndexB])

            colSum = valA + valB + carry
            colVal = colSum % 2
            carry = colSum / 2

            result.insert(0, colVal)
            lastIndexA -= 1
            lastIndexB -= 1

        if carry > 0:
            result.insert(0, 1)

        return ''.join(str(x) for x in result)
```