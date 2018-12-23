# Concept

以下方法會有記憶體問題，但比較簡單。從 2 開始，發現是質數就 +1，並且將他的倍數全部標記。

```py
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        primes = {}
        for i in range(2, n):
            if i not in primes:
                count += 1
                temp = i
                while temp <= n:
                    primes[temp] = False
                    temp += i

        return count
```
