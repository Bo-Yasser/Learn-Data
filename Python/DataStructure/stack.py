
# Stack Class
import numpy as np 
class Stack:

    def __init__(self, size, type="int"):
        self.__type = type
        self.__size = size
        self.__arr = np.empty(self.__size, dtype=self.__type)
        self.__top = -1
    
    def __str__(self):
        return f"Stack({self.disply()})"
    # Push Elements
    def push(self, data):
        if self.__top + 1 == self.__size:
            raise OverflowError("Stack Is Full.")
        if not isinstance(data, eval(self.__type)):
            raise TypeError(f"Data must be of type {self.__type}")
        
        self.__arr[self.__top + 1] = data            
        self.__top +=1

    
    # Pop Elements
    def pop(self, element=None):
        if self.is_empty():
           raise IndexError("Stack Is Empty on pop") 
        
        if element is None:
            popped_element = self.__arr[self.__top]
            self.__arr[self.__top] = eval(self.__type)(0)
            self.__top -= 1
            return popped_element
        
        found = False
        for i in range(self.__top + 1):
            if self.__arr[i] == element:
                found = True
                for g in range(i, self.__top):
                    self.__arr[g] = self.__arr[g + 1]
                self.__top -= 1
                break

        if not found:
            raise ValueError(f"Element {element} not found in the stack")
    
    # Show Top Element
    def top(self):
        if not self.is_empty():
            return f"{self.__top} -> '{self.__arr[self.__top]}'"
        
        raise IndexError("Stack Is Empty on top")
    
    # Return element in specific index
    def peek(self, index):
        if index < 0 or index > self.__top:
            raise IndexError("Index out of range")
        return self.__arr[index]
    
    # Return index for specific element
    def search(self, element):
        for i in range(self.__top + 1):
            if self.__arr[i] == element:
                return i
        return -1

    def reverse(self):
        self.__arr[:self.__top + 1] = self.__arr[:self.__top + 1][::-1]

    def sort(self, reverse=False):
        self.__arr[:self.__top + 1] = sorted(self.__arr[:self.__top + 1], reverse=reverse)

    # Show If Empty
    def is_empty(self):
        return self.__top < 0
    
    def is_full(self):
        return self.__top + 1 == self.__size
    
    def clear(self):
        self.__arr = np.empty(self.__size, dtype=self.__type)
        self.__top = -1
    
    # Show All Elements    
    def disply(self):
        return self.__arr[:self.__top + 1][::-1]

    # Show Size 
    def size(self):
        return self.__size

    def count(self):
        return self.__top + 1
        
    
if __name__ == "__main__":
    stack_int = Stack(5)
    print(stack_int.size())
    print(stack_int.is_empty())

    stack_int.push(1)
    stack_int.push(2)
    
    stack_int.push(3)
    stack_int.push(4)
    stack_int.push(5)
    print(stack_int)
    # stack_int.push(10)
    stack_int.pop(3)
    stack_int.pop(2)
    stack_int.pop()
    # stack_int.pop(20)


    print(stack_int.top())
    print(stack_int.disply())
    # stack_int.clear()
    
    # print(stack_int.is_empty())
    # print(stack_int.top())




