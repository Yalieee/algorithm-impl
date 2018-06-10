# Concept
前一階走一步上來 + 前兩階走兩步上來
```
f(n) = f(n-1) + f(n-2)
```

```py
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {}
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n]
```