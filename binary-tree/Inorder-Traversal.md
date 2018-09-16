# Concept
一直找到一個沒有 Left child 的節點，接著將他自己加到結果中，再從他的右邊繼續

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, node, res):
        if node is None:
            return

        self.inOrder(node.left, res)
        res.append(node.val)
        self.inOrder(node.right, res)

    def recursiveTraversal(self, root):
        res = []
        self.inOrder(root, res)
        return res

    def iterativeTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = []
        stack.append(root)
        current = root.left
        while stack or current:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                res.append(node.val)
                current = node.right

        return res
```