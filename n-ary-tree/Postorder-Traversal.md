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
    def postorderTraversal(self, root, res):
        if root is None:
            return

        for child in root.children:
            self.postorderTraversal(child, res)

        res.append(root.val)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.postorderTraversal(root, res)
        return res
```