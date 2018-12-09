# Concept
兩種方式
- 用頭尾兩個指標，遇到合法的字母就比較，不合法就繼續走
- 如下，將字串分別從頭尾正規化，再比較結果

```py
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalizeS = []
        for i in s:
            if i.isalpha() or i.isdigit():
                normalizeS.append(i.lower())

        normalizeR = []
        for i in s[::-1]:
            if i.isalpha() or i.isdigit():
                normalizeR.append(i.lower())

        return normalizeS == normalizeR
```