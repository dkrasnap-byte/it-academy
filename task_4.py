class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.val

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.val

    def is_empty(self) -> bool:
        return self.size == 0

    def size(self) -> int:
        return self.size


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    stack.push(3)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
