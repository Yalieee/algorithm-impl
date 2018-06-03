# Concept
先找出最短的字串，代表 prefix 最長就是這麼長，用來當 loop 的結束條件。

接著一次走一個字元，利用 set 來看是否存在兩種以上，如果是就終止

# Notice
Python 的 `Set` 無法直接存取第一個元素，因此要先用 List 儲存。

```py
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ''

        # find min length
        minLength = None
        for element in strs:
            if minLength is None:
                minLength = len(element)
            else:
                minLength = min(minLength, len(element))

        prefix = []
        for index in range(minLength):
            charList = []
            for element in strs:
                 charList.append(element[index])
            charSet = set(charList)
            if len(charSet) > 1:
                break
            prefix.append(charList[0])

        return ''.join(prefix)
```