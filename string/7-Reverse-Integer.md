# Notice
注意一些細節
- modulo 運算只能用在正數
- 縮減 x 時，要將它變成 int 而不是留在 float/double

```py
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1

        result = 0
        while x != 0:
            result *= 10
            digit = x % 10
            result += digit
            x = int(x / 10)

        if isNegative:
            result *= -1

        if result > 2147483647 or result < -2147483648:
            return 0

        return result
```