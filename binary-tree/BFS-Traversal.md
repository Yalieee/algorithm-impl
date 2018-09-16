# BFS Traversal

使用 queue

```py
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        queue.append((root, 1))

        while queue:
            (node, level) = queue.pop(0)

            if node is None:
                continue

            if len(res) < level:
                res.append([node.val])
            else:
                res[level-1].append(node.val)

            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        return res
```