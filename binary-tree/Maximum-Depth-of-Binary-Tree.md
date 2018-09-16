
```py
class Solution(object):
    def topDown(self, node, depth):
        if node is None:
            return depth

        leftDepth = depth
        rightDepth = depth
        if node.left is not None:
            leftDepth = self.topDown(node.left, depth+1)
        if node.right is not None:
            rightDepth = self.topDown(node.right, depth+1)

        return max(leftDepth, rightDepth)


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.topDown(root, 1)
```