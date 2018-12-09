# Concept
一樣用 HashMap 來解。這邊可以發現 Python 能夠直接比較兩個 dict

```py
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMapS = {}
        for char in s:
            if char in hashMapS:
                hashMapS[char] += 1
            else:
                hashMapS[char] = 1

        hashMapT = {}
        for char in t:
            if char in hashMapT:
                hashMapT[char] += 1
            else:
                hashMapT[char] = 1

        return hashMapS == hashMapT
```