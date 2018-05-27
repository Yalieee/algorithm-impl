## Concept
使用三個指標 prev, current, next
- prev 起始為 null
- current 起始為 head
- next 起始為 head.next

## Detail
1. 每次只做 `cuurent.next = prev`
2. 往前移動三個指標 (注意 next 是 null 時就要停下)
3. loop 直到 current 是 null
4. 最後 prev 會停在新的 Head

```py
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        prev = None
        cur = head
        nextP = head.next

        while cur:
            cur.next = prev
            prev = cur
            cur = nextP
            if nextP is not None:
                nextP = nextP.next
        return prev
```