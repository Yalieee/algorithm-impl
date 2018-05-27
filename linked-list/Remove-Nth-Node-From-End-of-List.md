# Concept
讓 Fast 指標走在 Slow 前面，距離是要刪掉的點的位子，當 Fast 走到底時，Slow 會停在要刪掉的點的前一個位子。

# Notice
Head 也有可能是要刪除對象，此時需要更新新的 Head 位置。此外為了方便刪除 Head 節點，可以在前面多準備一個點

```py
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(0)
        preHead.next = head
        fast = preHead
        slow = preHead
        for i in range(n):
            if fast.next is not None:
                fast = fast.next
            else:
                return None

        while fast and fast.next is not None:
            fast = fast.next
            slow = slow.next

        # node to delete is head
        if slow == preHead:
            return slow.next.next

        if slow.next is not None:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head
````