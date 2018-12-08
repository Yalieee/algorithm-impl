# Question
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Concept
注意這邊要回傳的是長度，不是 Index

用一個指標來紀錄要填的位置

```py
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        currentNum = None
        nextIndex = 0
        for ind, element in enumerate(nums):
            if element == currentNum:
                continue
            currentNum = element
            nums[nextIndex] = element
            nextIndex += 1

        return nextIndex
```