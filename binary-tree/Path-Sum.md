```py
class Solution(object):
    def topDown(self, node, parentSum, target):
        if node is None:
            return False

        newSum = node.val + parentSum
        if node.left is None and node.right is None and newSum == target:
            return True

        leftResult = self.topDown(node.left, newSum, target)
        rightResult = self.topDown(node.right, newSum, target)

        return leftResult or rightResult

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        return self.topDown(root, 0, sum)
```