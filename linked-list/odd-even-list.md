# Concept
用四個指標去維護奇數串和偶數串的頭尾，最後再把它們串起來即可。

# Notice
最後要把偶數的尾接到 None，否則會變成環狀 List 導致無限迴圈

```py
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        oddHead = head
        oddTail = head
        evenHead = head.next
        evenTail = head.next

        if evenHead.next is None:
            return head

        cur = evenHead.next
        number = 3
        while cur:
            if number % 2 == 0:
                evenTail.next = cur
                evenTail = cur
            else:
                oddTail.next = cur
                oddTail = cur
            cur = cur.next
            number += 1

        oddTail.next = evenHead
        evenTail.next = None

        return oddHead
```
