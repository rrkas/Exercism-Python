class Node:
    def __init__(self, value):
        self.val = value
        self.nxt = None

    def value(self):
        return self.val

    def next(self):
        return self.nxt

    def set_next(self, node):
        self.nxt = node


class LinkedList:
    def __init__(self, values=[]):
        self.head_node = None
        for value in values:
            if self.head_node is None:
                self.head_node = Node(value)
            else:
                t2 = Node(value)
                t2.set_next(self.head_node)
                self.head_node = t2

    def __len__(self):
        c = 0
        t = self.head_node
        while t is not None:
            t = t.next()
            c += 1
        return c

    def __iter__(self):
        return LinkedListIterator(self)

    def head(self):
        if self.head_node is None:
            raise EmptyListException(' ')
        return self.head_node

    def push(self, value):
        t = Node(value)
        t.set_next(self.head_node)
        self.head_node = t

    def pop(self):
        if self.head_node is None:
            raise EmptyListException(' ')
        t = self.head_node.value()
        self.head_node = self.head_node.next()
        return t

    def reversed(self):
        l = []
        t = self.head_node
        while t is not None:
            l.append(t.value())
            t = t.next()
        return l[::-1]


class EmptyListException(Exception):
    pass


class LinkedListIterator:
    def __init__(self, linkedList):
        self.ll_head = linkedList.head_node

    def __next__(self):
        if self.ll_head is None:
            raise StopIteration
        t = self.ll_head.value()
        self.ll_head = self.ll_head.next()
        return t
