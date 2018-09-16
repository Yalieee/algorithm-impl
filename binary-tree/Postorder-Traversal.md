# Postorder traversal

https://youtu.be/xLQKdq0Ffjg

注意最後那個 while

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
        res = []
        stack = []
        current = root

        while stack or current:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                node = stack[-1] # peak

                if node.right is not None:
                    current = node.right
                else:
                    node = stack.pop()
                    res.append(node.val)
                    while stack and node == stack[-1].right:
                        node = stack.pop()
                        res.append(node.val)
```
