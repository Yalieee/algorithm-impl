class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.count:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next

        if cur is None:
            return -1

        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode
        self.count += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newNode = Node(val)

        # find tail element
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
        self.count += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.count:
            return

        # find prev element
        cur = self.head
        for i in range(index-1):
            cur = cur.next

        newNode = Node(val)
        if cur is None:
            self.head = newNode
        else:
            newNode.next = cur.next
            cur.next = newNode

        self.count += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index > self.count:
            return

        # find prev element
        cur = self.head
        for i in range(index-1):
            cur = cur.next

        if cur is None:
            return
        if cur.next is None:
            cur.next = None
        else:
            cur.next = cur.next.next

    def printAll(self):
        cur = self.head
        while cur:
            print cur.val
            cur = cur.next
