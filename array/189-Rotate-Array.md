# Concept
方法很多，這是比較簡單的方法

```py
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        for i in range(k):
            num = nums.pop()
            nums.insert(0, num)
```