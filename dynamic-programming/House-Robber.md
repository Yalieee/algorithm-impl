# Concept
```
maxProfit(n) = max(maxProfit(n-1), maxProfit(n-2) + nums[n])
```

```py
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if not nums or length == 0:
            return 0
        if length == 1:
            return nums[0]

        maxProfit = {}
        maxProfit[0] = nums[0]
        maxProfit[1] = max(nums[0], nums[1])

        for n in range(2, length):
            maxProfit[n] = max(maxProfit[n-1], maxProfit[n-2] + nums[n])

        return maxProfit[length-1]
```