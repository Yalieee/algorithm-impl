# Concept
用一個 hash map 記錄前一次出現的紀錄。當發現重複的字元出現時，就可以將字串的起點從重複字元的下一個開始起跳(因為不會有更長的了)。

注意兩個 Max 都要有

```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0
        hashMap = {}
        for i in range(len(s)):
            if s[i] in hashMap:
                start = max(hashMap[s[i]] + 1, start)
            hashMap[s[i]] = i
            maxLen = max(maxLen, i - start + 1)

        return maxLen
```