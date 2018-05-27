# Concept
大原則和正常的 remove 一樣。

要注意的只有 Head 有可能被移除，因此一樣需要在 head 前面建立一個節點來處理，並更新 head 指標

```py
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        preHead = ListNode(0)
        preHead.next = head

        newHead = head
        cur = preHead
        while cur.next:
            if cur.next.val == val:
                if cur.next == newHead:
                    newHead = newHead.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        return newHead
```