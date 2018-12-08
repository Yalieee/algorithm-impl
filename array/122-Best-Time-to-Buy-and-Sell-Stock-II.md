# Concept
和 I 不一樣，不用等到最高點在賣，只要比較高就當場賣出重新買進就好

```py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        buyPoint = prices[0]
        finalProfit = 0
        for price in prices[1:]:
            profit = price - buyPoint
            if profit > 0:
                finalProfit += profit

            buyPoint = price

        return finalProfit
```