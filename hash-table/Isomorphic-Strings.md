# Concept
建立一個 S 到 T 的 hashMap，走的過程檢查之前出現過的字是否仍然一致的對應。

接著由於有個限制是 `No two characters may map to the same character but a character may map to itself.` ，因此要考慮以下 case
```
s = 'ab'
t = 'aa'
```
此時走完會發現產生一個這樣的表 `{'a': 'a', 'b': 'a'}`，並且中途不會回傳 False。因此最後要檢查是否有兩個 char 重複對應到同個字

```py
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False

        hashMap = {}

        for i in range(lenS):
            charS = s[i]
            charT = t[i]

            if charS in hashMap:
                if charT != hashMap[charS]:
                    return False
            else:
                hashMap[charS] = charT

        hashValues = hashMap.values()

        return len(hashValues) == len(set(hashValues))
```
