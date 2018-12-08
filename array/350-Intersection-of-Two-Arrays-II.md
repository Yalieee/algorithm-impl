# Concept
照直覺用 map 操作即可

```py
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        for num in nums1:
            if num not in map1:
                map1[num] = 1
            else:
                map1[num] += 1

        result = []
        for num in nums2:
            if num in map1 and map1[num] > 0:
                map1[num] -= 1
                result.append(num)

        return result
```