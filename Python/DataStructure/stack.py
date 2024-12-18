
# Stack Class
import numpy as np 
class Stack:

    def __init__(self, size, type="int"):
        self.__type = type
        self.__size = size
        self.__arr = np.empty(self.__size, dtype=self.__type)
        self.__top = -1
    
    def __str__(self):
        return f"Stack({self.display()})"
    
    # Push Elements
    def push(self, data):
        if self.__top + 1 == self.__size:
            raise OverflowError("Stack Is Full.")
        
        if not isinstance(data, eval(self.__type)):
            raise TypeError(f"Data must be of type {self.__type}")
        
        self.__top +=1
        self.__arr[self.__top] = data            

    
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
                
                self.__arr[self.__top] = eval(self.__type)(0)
                self.__top -= 1
                break

        if not found:
            raise ValueError(f"Element {element} not found in the stack")
    
    # Show Top Element
    def top(self):
        if not self.is_empty():
            return self.__arr[self.__top]
        
        raise IndexError("Stack Is Empty on top")
    
    def merge(self, other_stack):
        if not isinstance(other_stack, Stack):
            raise TypeError("Can only merge with another Stack.")
        
        if self.__type != other_stack.__type:
            raise TypeError(f"Cannot merge stacks with different types: {self.__type} and {other_stack.__type}")
        
        new_size = self.__top + 1 + other_stack.count()
        if new_size > self.__size:
            raise OverflowError("Not Enough Space To Merge Stacks.")
        
        for i in range(other_stack.count()):
            self.push(other_stack.peek(i))

    # Return element in specific index
    def peek(self, index):
        if index < 0 or index > self.__top:
            raise IndexError("Index out of range")
        return eval(self.__type)(self.__arr[index])
    
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
        self.__arr[:self.__top + 1] = eval(self.__type)(0)
        self.__top = -1

    # Show All Elements    
    def display(self):
        return self.__arr[:self.__top + 1][::-1]

    # Show Size 
    def size(self):
        return self.__size

    def count(self):
        return self.__top + 1
        
    
if __name__ == "__main__":
    # stack_int = Stack(7)
    # stack2 = Stack(4)
    # print(stack_int.size())
    # print(stack_int.is_empty())

    # stack_int.push(1)
    # stack_int.push(2)
    
    # stack_int.push(3)
    # stack_int.push(4)
    # stack_int.push(5)
    # print(stack_int)
    # # stack_int.push(10)
    # stack_int.pop(3)
    # # stack_int.pop(2)
    # # stack_int.pop()
    # # stack_int.pop(20)


    # print(stack_int.top())
    
    # print(stack_int.display())
    # # stack_int.clear()
    # stack2.push(10)
    # stack2.push(20)
    # print(stack2.display())

    # stack_int.merge(stack2)
    
    # print(stack_int.display())
    
    # # print(stack_int.is_empty())
    # print(stack_int.top())
    
    
    # Balanced Parentheses Using Stack
    def are_pair(open, close):
        if open == "(" and close == ")":
            return True
        elif open == "{" and close == "}":
            return True
        elif open == "[" and close == "]":
            return True
        return False

    def are_balanced(exp):
        exp = str(exp)
        stack = Stack(100, "str")
        for i in range(len(exp)):
            if exp[i] == "(" or exp[i] == "{" or exp[i] == "[":
                stack.push(exp[i])
            elif exp[i] == ")" or exp[i] == "}" or exp[i] == "]":
                if stack.is_empty() or not are_pair(stack.top(), exp[i]):
                    return False
                stack.pop()
        
        return stack.is_empty()
    
    # print(are_balanced("(){}[]"))
    # print(are_balanced("(){}[]()[[{()}]]"))
    # print(are_balanced("(){]((]{{"))
    # print(are_balanced("][}{"))

