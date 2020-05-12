# Implementation of Stacks

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
print (s.isEmpty())

s.push(1)
s.push('two')
s.push(True)
print(s.peek())
print(s.size())
print(s.isEmpty())
print(s.size())

print(s.pop())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.isEmpty())

    

