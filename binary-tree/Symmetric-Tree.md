```py
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        leftQueue = []
        rightQueue = []

        if root is None:
            return True

        leftQueue.append(root.left)
        rightQueue.append(root.right)

        while leftQueue and rightQueue:
            if len(leftQueue) == 0:
                return False
            leftNode = leftQueue.pop()

            if len(rightQueue) == 0:
                return False
            rightNode = rightQueue.pop()

            if leftNode is None and rightNode is not None:
                return False
            if rightNode is None and leftNode is not None:
                return False

            if leftNode and rightNode and leftNode.val != rightNode.val:
                return False

            if leftNode:
                leftQueue.append(leftNode.left)
                leftQueue.append(leftNode.right)

            if rightNode:
                rightQueue.append(rightNode.right)
                rightQueue.append(rightNode.left)

        return True
```
