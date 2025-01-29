class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.__head = None
        self.__top = -1

    def __str__(self):
        return f"Stack({list(self)})"
    
    def __iter__(self):

        current = self.__head
        while current:
            yield current.value
            current = current.next
    
    def __contains__(self, value):
        return self.is_found(value)
    
    def search(self, element):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        
        current = self.__head
        count = self.__top 
        while current:
            if current.value == element:
                return count
            current = current.next
            count -= 1
        return f"{element} not found."
    

    def peek(self, index):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        
        if index > self.__top or index < 0:
            raise IndexError("Index Out Of Range.")
        
        current = self.__head
        count = self.__top 
        while current:
            if count == index:
                return current.value
            current = current.next
            count -= 1
        raise IndexError("element not found.")
    
    def push(self, value):
        new_node = Node(value)
        
        new_node.next = self.__head
        self.__head = new_node
        self.__top += 1
        
    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("Stack Is Empty. Nothing to Pop.")


        if value is None or self.__head.value == value:
            popped_value = self.__head.value
            self.__head = self.__head.next
            self.__top -= 1
            return popped_value

        current = self.__head
        while current.next:
            if current.next.value == value:
                popped_value = current.next.value
                current.next = current.next.next
                self.__top -= 1
                return popped_value
            current = current.next

        raise IndexError(f"Value {value} not found in the stack.")

    def sort(self, reverse=False):
        values = list(self)
        values.sort(reverse=reverse)
        self.clear()
        for value in reversed(values):
            self.push(value)
    
    def is_sorted(self):
        current = self.__head
        while current and current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True

    def merge(self, other_stack):
        if not isinstance(other_stack, LinkedStack):
            raise TypeError("must merge stack with another stack.")
        for value in reversed(list(other_stack)):
            self.push(value)

    def reverse(self):
        current = self.__head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev
    
    def display(self):
        return list(self)
    
    def clear(self):
        self.__head = None
        self.__top = -1
    
    def is_empty(self):
        return self.__head == None
    
    def is_found(self, element):
        current = self.__head
        while current:
            if current.value == element:
                return True
            current = current.next
        return False    
    
    def count(self):
        return self.__top + 1

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.__head.value
    





if __name__ == "__main__":
    stack = LinkedStack()
    stack2= LinkedStack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop(20)
    print(stack.top())
    print(stack.display())

    print("#"* 50)
    stack.pop()
    stack.push(30)
    stack.push(40)
    print(stack.top())
    print(stack.display())

    print("#"* 50)
    print(stack.peek(0))
    print(stack.search(40))

    print("#"* 50)
    stack.reverse()
    print(stack.display())
    print(stack.top())

    print("#"* 50)
    print(stack.peek(0))
    print(stack.search(40))

    stack.sort()
    print(stack.is_sorted())
    print(stack.display())

    # print("#"* 50)
    # print("#"* 50)

    # stack2.push(400)
    # stack2.push(300)
    # print(stack2.display())
    # print(stack.top())

    # stack.merge(stack2)
    # print(stack.display())
    # print(stack.top())

    # print("#"* 50)
    # print("#"* 50)
    
    # print(stack)
    # for i in stack:
    #     print(i, end='-')
    # if 10 in stack:
    #     print("\na4ta")