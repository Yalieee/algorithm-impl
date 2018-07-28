# Concept
如果 input 是  array，可以直接 O(1) 取得中間點，但 List 的話無法，因此需要用快慢指標來找。
此外在用遞迴分割時，不像 array 可以直接分割 input，List 要分割需要改變 next 指標來做到。

```py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMidNodeAndPrevious(self, lst):
        fast = slow = prev = lst
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        return slow, prev

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        midNode, prevNode = self.findMidNodeAndPrevious(head)
        node = TreeNode(midNode.val)
        prevNode.next = None

        if head != midNode:
            node.left = self.sortedListToBST(head)
        else:
            node.left = None

        node.right = self.sortedListToBST(midNode.next)

        return node
```