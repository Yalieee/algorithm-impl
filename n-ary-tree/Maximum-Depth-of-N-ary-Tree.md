# Note
注意一下起始 Level 是 1，然後可以用 `max()` 取得 List 中最大的數字

```py
class Solution(object):
    def _maxDepth(self, root, level):
        res = []
        for child in root.children:
            childLevel = self._maxDepth(child, level+1)
            res.append(childLevel)

        if res:
            return max(res)
        return level

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        level = 1

        if root is None:
            return 0

        res = []
        for child in root.children:
            childLevel = self._maxDepth(child, level+1)
            res.append(childLevel)

        if res:
            return max(res)
        return level
```
