# Concept
一直找到一個沒有 Left child 的節點，接著將他自己加到結果中，再從他的右邊繼續

詳細步驟
1. Create an empty stack S.
2. Initialize current node as root
3. Push the current node to S and set current = current->left until current is NULL
4. If current is NULL and stack is not empty then
    - Pop the top item from stack.
    - Print the popped item, set current = popped_item->right
    - Go to step 3.
5. If current is NULL and stack is empty then we are done.

Ref
- https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

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