```py
class Solution(object):
    def postOrder(self, node, res):
        if node is None:
            return

        self.postOrder(node.left, res)
        self.postOrder(node.right, res)
        res.append(node.val)

    def recursiveTraversal(self, root):
        res = []
        self.postOrder(root, res)
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = []
        prev = None
        stack.append(root)
        while stack:
            node = stack[-1]  # peek

            if prev is None or prev.left == node or prev.right == node:
                if node.left is not None:
                    stack.append(node.left)
                elif node.right is not None:
                    stack.append(node.right)
            elif prev == node.left:
                if node.right is not None:
                    stack.append(node.right)
            else:
                res.append(node.val)
                stack.pop()
            prev = node

        return res
```
