# Concept
每次都重做的話會超時，因此把之前的計算結果存起來即可

```py
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []

        summation = 0
        for i in nums:
            summation += i
            self.sums.append(summation)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i-1 < 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```