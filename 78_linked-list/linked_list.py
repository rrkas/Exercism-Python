class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.val = value
        self.prev = previous
        self.next = succeeding


class LinkedList:
    def __init__(self):
        self.head_node = None

    def push(self, param):
        t = self.head_node
        while t is not None and t.next is not None:
            t = t.next
        if t is None:
            self.head_node = Node(param)
        else:
            t.next = Node(param)

    def shift(self):
        t = self.head_node.val
        self.head_node = self.head_node.next
        return t

    def pop(self):
        t = self.head_node
        while t is not None and t.next is not None and t.next.next is not None:
            t = t.next
        if t is None:
            raise ValueError(' ')
        if t.next:
            t2 = t.next
            t.next = None
            return t2.val
        else:
            v = t.val
            self.head_node = None
            return v

    def unshift(self, param):
        t = Node(param)
        t.next = self.head_node
        self.head_node = t

    def __iter__(self):
        return LinkedListIterator(self)

    def __len__(self):
        c = 0
        t = self.head_node
        while t is not None:
            c += 1
            t = t.next
        return c

class LinkedListIterator:
    def __init__(self, ll):
        self.ll_head = ll.head_node

    def __next__(self):
        if self.ll_head is None:
            raise StopIteration
        t = self.ll_head.val
        self.ll_head = self.ll_head.next
        return t