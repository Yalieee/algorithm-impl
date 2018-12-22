# Concept
窮舉類的題目基本上都使用遞迴處理。

# Notice
要注意在傳遞 nums 時，每次傳遞不能用 call by reference

```py
class Solution(object):
    def generate(self, nums, partialResult, res):
        if not nums:
            res.append(partialResult)

        for index in range(len(nums)):
            self.generate(nums[:index] + nums[index+1:], partialResult + [nums[index]], res)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.generate(nums[:], [], res)
        return res
```