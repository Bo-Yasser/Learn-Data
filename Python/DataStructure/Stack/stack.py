
# Stack Class
import numpy as np 
class Stack:

    def __init__(self, size, dtype="int"):
        self.__dtype = dtype
        self.__size = size
        self.__arr = np.empty(self.__size, dtype=self.__dtype)
        self.__default_value = self.__arr[0]
        self.__top = -1
    
    # return readable str when print the object
    def __str__(self):
        return f"Stack({self.display()})"
    
    # support iteration for any stack object
    def __iter__(self):
        reversed_stack = self.__arr[:self.__top + 1][::-1]
        return iter(reversed_stack)
    
    # support in condition
    def __contains__(self, value):
        return self.is_found(value)
    
    # Push Elements
    def push(self, data):
        if self.__top + 1 == self.__size:
            raise OverflowError("Stack Is Full.")
        
        if not np.issubdtype(type(data), np.dtype(self.__dtype).type):
            raise TypeError(f"Data must be of type {self.__dtype}")
        
        self.__top +=1
        self.__arr[self.__top] = data            

    
    # Pop Elements
    def pop(self, element=None):
        if self.is_empty():
           raise IndexError("Stack Is Empty on pop") 
        
        if element is None:
            popped_element = self.__arr[self.__top]
            self.__arr[self.__top] = self.__default_value
            self.__top -= 1
            return popped_element
        
        found = False
        for i in range(self.__top + 1):
            if self.__arr[i] == element:
                found = True
                for g in range(i, self.__top):
                    self.__arr[g] = self.__arr[g + 1]
                
                self.__arr[self.__top] = self.__default_value
                self.__top -= 1
                break

        if not found:
            raise ValueError(f"Element {element} not found in the stack")
    
    # Show Top Element
    def top(self):
        if not self.is_empty():
            return self.__arr[self.__top]
        
        raise IndexError("Stack Is Empty on top")
    
    # merge with another stack
    def merge(self, other_stack):
        if not isinstance(other_stack, Stack):
            raise TypeError("Can only merge with another Stack.")
        
        if self.__dtype != other_stack.__dtype:
            raise TypeError(f"Cannot merge stacks with different types: {self.__dtype} and {other_stack.__dtype}")
        
        new_size = self.__top + 1 + other_stack.count()
        if new_size > self.__size:
            raise OverflowError("Not Enough Space To Merge Stacks.")
        
        for i in range(other_stack.count()):
            self.push(other_stack.peek(i))

    # Return element in specific index
    def peek(self, index):
        if index < 0 or index > self.__top:
            raise IndexError("Index out of range")
        return self.__arr[index]
    
    # reverse stack
    def reverse(self):
        self.__arr[:self.__top + 1] = self.__arr[:self.__top + 1][::-1]

    # sort stack 
    def sort(self, reverse=False):
        self.__arr[:self.__top + 1] = sorted(self.__arr[:self.__top + 1], reverse=reverse)

    def is_sorted(self):
        for i in range(self.__top + 1):
            if self.__arr[i] > self.__arr[i + 1]:
                return False
        return True 

    # Show If stack is empty
    def is_empty(self):
        return self.__top < 0
    
    # Show If stack is full
    def is_full(self):
        return self.__top + 1 == self.__size
    
    # Return index for specific element
    def search(self, element):
        for i in range(self.__top + 1):
            if self.__arr[i] == element:
                return i
        return -1
    
    # Return True if found and False if not found
    def is_found(self, element):
        for i in range(self.__top + 1):
            if self.__arr[i] == element:
                return True
        return False
    
    # clear stack
    def clear(self):
        self.__arr[:self.__top + 1] = self.__default_value
        self.__top = -1

    # Show All Elements    
    def display(self):
        return self.__arr[:self.__top + 1][::-1]

    # Show Size 
    def size(self):
        return self.__size
    
    # return length for stack
    def count(self):
        return self.__top + 1
    
    def resize(self, new_size):
        if new_size <= self.__size:
            raise ValueError("new size must be larger than current size.")
        
        new_arr = np.empty(new_size ,dtype=self.__dtype)
        for i in range(self.__top + 1):
            new_arr[i] = self.__arr[i]
        
        self.__arr = new_arr
        self.__size = new_size
        
    
         

if __name__ == "__main__":
    stack = Stack(5)

    stack.push(5)
    stack.push(4)
    stack.push(3)

    print(stack.peek(1))
    print(stack.display())
    print(stack)
    stack.sort()
    print(stack.display())
    print(stack.top())
    print(stack.is_sorted())
