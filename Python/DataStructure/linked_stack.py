class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
        self.__top = -1


    def search(self, element):
        current = self.head
        count = self.__top 
        while current:
            if current.value == element:
                return count
            current = current.next
            count -= 1
        return -1
    

    def peek(self, index):
        if index > self.__top or index < 0:
            raise IndexError("Index Out Of Range.")
        
        current = self.head
        count = self.__top 
        while current:
            if count == index:
                return current.value
            current = current.next
            count -= 1

        raise IndexError("Index Out of Range.")
    
    
    def push(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
        self.__top += 1
        
    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("Stack Is Empty. Nothing to Pop.")


        if value is None or self.head.value == value:
            popped_value = self.head.value
            self.head = self.head.next
            self.__top -= 1
            return popped_value

        current = self.head
        while current.next:
            if current.next.value == value:
                popped_value = current.next.value
                current.next = current.next.next
                self.__top -= 1
                return popped_value
            current = current.next

        raise ValueError(f"Value {value} not found in the stack.")

    def sort(self, reverse=False):
        values = []
        while not self.is_empty():
            values.append(self.pop())
            values.sort(reverse=reverse)
        
        for val in values:
            self.push(val)
    
    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.value < current.next.value:
                return False
            current = current.next
        return True
    
    def merge(self, other_stack):
        temp = []
        current = other_stack.head
        while current:
            temp.append(current.value)
            current = current.next


        for value in reversed(temp):
            self.push(value)

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display(self):
        current = self.head
        if not current:
            print("Stack is Empty.")
            return
        
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def clear(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def count(self):
        return self.__top + 1
    
    def top(self):
        if not self.is_empty():
            return f"{self.__top} ->({self.head.value})"
    
    def size(self):
        return self.__top + 1




if __name__ == "__main__":
    stack = LinkedStack()
    stack2= LinkedStack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop(20)
    print(stack.top())
    stack.display()

    print("#"* 50)
    stack.pop()
    stack.push(30)
    stack.push(40)
    print(stack.top())
    stack.display()

    print("#"* 50)
    print(stack.peek(0))
    print(stack.search(40))

    print("#"* 50)
    stack.reverse()
    stack.display()
    print(stack.top())

    print("#"* 50)
    print(stack.peek(0))
    print(stack.search(40))

    stack.sort()
    print(stack.is_sorted())
    stack.display()

    print("#"* 50)
    print("#"* 50)

    stack2.push(400)
    stack2.push(300)
    stack2.display()
    print(stack.top())

    stack.merge(stack2)
    stack.display()
    print(stack.top())


