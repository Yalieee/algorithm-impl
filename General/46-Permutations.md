# Concept
窮舉類的題目基本上都使用遞迴處理。

# Notice
要注意在傳遞 nums 和 partialResult 時，每次傳遞不能用 call by reference

```py
class Solution(object):
    def generate(self, nums, partialResult, res):
        if not nums:
            if partialResult:
                res.append(partialResult)
            return

        for index in range(len(nums)):
            output = []
            if partialResult is None:
                output = [nums[index]]
            else:
                output = partialResult + [nums[index]]

            self.generate(nums[:index] + nums[index+1:], output, res)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.generate(nums[:], None, res)
        return res
```