# Concept
先算有幾個 0，再把他補到後面

```py
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numZero = 0
        lastIndex = 0

        for k, v in enumerate(nums):
            if v == 0:
                numZero += 1
            else:
                nums[lastIndex] = v
                lastIndex += 1

        for i in range(numZero):
            nums[lastIndex] = 0
            lastIndex += 1
```