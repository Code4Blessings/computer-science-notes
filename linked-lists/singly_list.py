class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    current = head
    prev = None
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = prev
        prev = current
        current = prev

    return prev


