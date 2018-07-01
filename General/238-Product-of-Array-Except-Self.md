# 暴力法
直覺使用暴力法，明顯會超時
```py
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for i in range(len(nums)):
            product = 1
            for k,v in enumerate(nums):
                if k != i:
                    product *= v
            output.append(product)

        return output
```

# Space O(1)
概念取自[這裡](http://www.cnblogs.com/grandyang/p/4650187.html)

每個位置的答案 = 他的左邊的乘積 x 他的右邊的乘積

因此 O(n) 的做法，是分別從左到右及從右到左儲存一份乘積。而 O(1) 的作法，則是把左邊的乘積直接放到 output 陣列中，之後再從右邊用一個變數計算乘積。

```py
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        prev = 1
        for element in nums:
            product = prev * element
            output.append(product)
            prev = product

        rightProduct = 1
        for index in range(len(nums)-1, -1, -1):
            if index -1 >= 0:
                output[index] = output[index-1] * rightProduct
            else:
                output[index] = rightProduct
            rightProduct *= nums[index]


        return output
```
