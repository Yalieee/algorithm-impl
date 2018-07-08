# Concept
找兩個的交集。

先把其中一個轉成 hash set，接著走第二個看是否出現在 set 中

```py
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashSet = set(nums1)

        result = set();
        for i in nums2:
            if i in hashSet:
                result.add(i)

        return list(result)
```