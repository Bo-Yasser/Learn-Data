import numpy as np
class Array:

    def __init__(self, size, dtype="int"):
        self.__size = size
        self.__dtype = dtype
        self.__arr = np.empty(self.__size, dtype=self.__dtype)
        self.__default_value = self.__arr[0]
        self.__count = 0

    
    def __str__(self):
        return f"Array({self.display()})"
    
    def __iter__(self):
        return iter(self.__arr[:self.__count])

    def __contains__(self, value):
        return self.is_found(value)  
    
    def is_empty(self):
        return self.__count == 0
    
    def is_full(self):
        return self.__count == self.__size
    
    def is_found(self, value):
        if self.is_empty():
            raise IndexError("Array is empty.")
        
        if self.search(value) == -1:
            return False
        
        return True
    
    def size(self):
        return self.__size
    
    def count(self):
        return self.__count
    
    def search(self, value):
        if self.is_empty():
            raise IndexError("Array is empty.")
        
        for i in range(self.__count):
            if self.__arr[i] == value:
                return i
        return -1
    
    def peek(self, index):
        if self.is_empty():
            raise IndexError("Array is empty.")
        
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of range.")
        
        return self.__arr[index]
    
    def display(self):
        return [self.__arr[i].item() for i in range(self.__count)]
    
    
    def insert_first(self, value):
        if self.is_full():
            raise OverflowError("Array is Full.")
        if not np.issubdtype(type(value), np.dtype(self.__dtype).type):
            raise TypeError(f"Data must be of type {self.__dtype}") 
        
        for i in range(self.__count, 0, -1):
            self.__arr[i] = self.__arr[i - 1]

        self.__arr[0] = value
        self.__count += 1 

    
    def insert_at_pos(self, pos, value):
        if self.is_full():
            raise OverflowError("Array is Full.")
        if pos < 1 or pos > self.__count:
            raise IndexError("Index out of range.")
        if not np.issubdtype(type(value), np.dtype(self.__dtype).type):
            raise TypeError(f"Data must be of type {self.__dtype}")
        
        if pos == 1:
            self.insert_first(value)
            return
        
        for i in range(self.__count, pos - 1, -1):
            self.__arr[i] = self.__arr[i - 1]
        
        self.__arr[pos - 1] = value
        self.__count += 1 


    def insert_last(self, value):
        if self.is_full():
            raise OverflowError("Array is Full.")
        if not np.issubdtype(type(value), np.dtype(self.__dtype).type):
            raise TypeError(f"Data must be of type {self.__dtype}")
        
        self.__arr[self.__count] = value
        self.__count += 1

    
    def insert_no_duplicate(self, value):
        if self.is_full():
            raise OverflowError("Array is Full.")
        if not np.issubdtype(type(value), np.dtype(self.__dtype).type):
            raise TypeError(f"Data must be of type {self.__dtype}")
        
        if self.search(value) == -1:
            self.insert_last(value)
            return

        return "Element already in Array."
  
    def fill(self, num_elements, elements):

        if num_elements + self.__count > self.__size:
            raise OverflowError("Number of Elements exceeds Array Size!")
        
        if len(elements) != num_elements:
            raise IndexError(f"must fill {num_elements} elements forget to fill {num_elements - len(elements)}")
        for x, value in enumerate(elements):
            if x >= num_elements: 
                break
            if not np.issubdtype(type(value), np.dtype(self.__dtype).type):
                raise TypeError(f"Data must be of type {self.__dtype}")

            self.__arr[self.__count + x] = value

        self.__count += num_elements

    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("Array is empty.")
        
        if value is None:
            popped_value = self.__arr[self.__count - 1]
            self.__arr[self.__count - 1] = self.__default_value
            self.__count -= 1
            return popped_value
        
        if self.__arr[0] == value:
            self.remove_first()
            return  
        
        found = False
        for i in range(self.__count):
            if self.__arr[i] == value:
                found = True
                for g in range(i, self.__count):
                    self.__arr[g] = self.__arr[g + 1]
                
                self.__arr[self.__count - 1] = self.__default_value 
                self.__count -= 1
                break
        if not found:
            raise ValueError(f"Element {value} not found in the Array.")
        
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Array is empty.")
        
        for i in range(self.__count - 1):
            self.__arr[i] = self.__arr[i + 1]
            
        self.__arr[self.__count - 1] = self.__default_value 
        self.__count -= 1

    def remove_at_pos(self, pos):
        if self.is_empty():
            raise OverflowError("Array is empty.")
        if pos < 1 or pos > self.__count:
            raise IndexError("Index out of range.")
        
        for i in range(pos - 1, self.__count - 1):

            self.__arr[i] = self.__arr[i + 1]
        
        self.__arr[self.__count - 1] = self.__default_value 
        self.__count -= 1

        
    def reverse(self):
        if self.is_empty():
            raise OverflowError("Array is empty.")
        self.__arr[:self.__count] = self.__arr[:self.__count][::-1]

    def sort(self, reverse=False):
        if self.is_empty():
            raise OverflowError("Array is empty.")
        self.__arr[:self.__count] = sorted(self.__arr[:self.__count], reverse=reverse)
         
    def is_sorted(self):
        if self.is_empty():
            raise OverflowError("Array is empty.")
        
        for i in range(self.__count):
            if self.__arr[i] > self.__arr[i + 1]:
                return False
        return True
    
    def merge(self, other_arr):
        if not isinstance(other_arr, Array):
            raise TypeError("must merge Array with another Array.")
        
        if self.__dtype != other_arr.__dtype:
            raise TypeError(f"Cannot merge Arrays with different types: {self.__dtype} and {other_arr.__dtype}")        
        
        new_size = self.__count + other_arr.count()
        if new_size > self.__size:
            raise OverflowError("Not Enough Space To Merge Stacks.")

        self.__arr[self.__count:] = other_arr.__arr[:other_arr.__count]
        self.__count = new_size


    def resize(self, new_size):
        if new_size <= self.__size:
            print("New size must be greater than the current size.")
            return
        new_arr = np.empty(new_size, dtype=self.__dtype)

        for i in range(self.__count):
            new_arr[i] = self.__arr[i]
        
        self.__arr = new_arr
        self.__size = new_size          






if __name__ == "__main__":
    arr = Array(5)
    arr.fill(5, [1,2,3,4,5])
    arr.pop(3)
    print(arr.display())

