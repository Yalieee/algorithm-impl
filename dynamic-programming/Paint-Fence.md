# Concept
Reference
- http://yuanhsh.iteye.com/blog/2219891

定義
- T(N): N 根柱子有幾種塗法 (答案要的)
- S(N): 第 N 根柱子和 N-1 顏色相同時有幾種塗法
- D(N): 第 N 根柱子和 N-1 顏色不同時有幾種塗法

顯然 T(N) = S(N) + D(N)

S(N) 因為和前一個相同，因此前一個一定和更前一個不同
- S(N) = D(N-1)

D(N) 因為和前一個不同，因此前一個有 K 種塗法時，這邊只會有 K-1 種
- D(N) = (K-1) * T(N-1)

綜合以上
```
T(N) = D(N-1)           + ((K-1) * T(N-1))
     = ((K-1) * T(n-2)) + ((K-1) * T(N-1))
     = (k-1) * (T(n-2) + T(n-1))
```

```py
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        ways = {}
        ways[0] = 0
        ways[1] = k
        ways[2] = k*k

        for i in range(3, n+1):
            ways[i] = (k-1) * (ways[i-1] + ways[i-2])

        return ways[n]
````