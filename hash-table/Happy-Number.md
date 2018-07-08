# Concept
建立一個 HashSet 來儲存之前算過的結果，當發現重複時代表開始 loop 了，回傳 False

```py
class Solution(object):
    def getDigits(self, n):
        res = []
        while n:
            res.insert(0, n % 10)
            n /= 10
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashSet = set()

        digits = self.getDigits(n)

        summ = 0
        while summ != 1:
            summ = 0
            for digit in digits:
                summ += digit * digit

            if summ in hashSet:
                return False

            hashSet.add(summ)
            digits = self.getDigits(summ)

        return True
```
