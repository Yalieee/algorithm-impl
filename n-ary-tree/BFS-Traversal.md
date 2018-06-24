# Note
注意最後要呈現的輸出格式如下，要用 level 控制 res 時，須注意一開始怎麼初始化每層的陣列
```json
[
     [1],
     [3,2,4],
     [5,6]
]
```

```py
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        queue = []

        if root is not None:
            queue.append((root, 0))  # 0 is level

        while queue:
            node, level = queue.pop(0)

            if len(res) - 1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            for child in node.children:
                # print node.val, child.val
                queue.append((child, level + 1))

        return res
```