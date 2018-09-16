

```py
class Solution(object):

    def _recursive(self, node, res):
        if node is None:
                return
        res.append(node.val)
        self._recursive(node.left, res)
        self._recursive(node.right, res)

    def recursiveTraversal(self, root):
        res = []
        self._recursive(root, res)
        return res

    def iterativeTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return res
```