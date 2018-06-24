# TODO
缺 Iterative 版本

```py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorderTraversal(self, root, res):
        if root is None:
            return

        res.append(root.val)
        for child in root.children:
            self.preorderTraversal(child, res)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.preorderTraversal(root, res)

        return res
```
