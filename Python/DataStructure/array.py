# Array Class

import numpy as np
class Array:

    def __init__(self, size, dtype="int"):
        self.__dtype = dtype
        self.__size = size
        self.__arr = np.empty(self.__size, dtype=self.__dtype)
        self.__default_value = self.__arr[0]
        self.__count = 0
    
    def __str__(self):
        if self.is_empty():
            return "Array is empty."
        return f"Array{self.display()}"
    
    def __iter__(self):
        return iter(self.__arr[:self.__count])
    
    def __contains__(self, value):
        return self.is_found(value)

    def resize(self, new_size):

        if new_size <= self.__size:
            print("New size must be greater than the current size.")
            return
        new_arr = np.empty(new_size, dtype=self.__dtype)

        for i in range(self.__count):
            new_arr[i] = self.__arr[i]
        
        self.__arr = new_arr
        self.__size = new_size           

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

            self.__arr[self.__count + x] = eval(self.__dtype)(value)

        self.__count += num_elements

    def append(self, value):
        if self.__arr is None:
            raise ValueError("Array not initialized. Please create the array first.")
        
        if self.__count < self.__size:
            self.__arr[self.__count] = value
            self.__count +=1

        else:
            raise OverflowError("Array Is Full!")    
           
    def insert(self, index, value):

        if self.__count >= self.__size:
            raise OverflowError("Array is full. Cannot insert.")
        if index >= self.__size:
            raise OverflowError("Index Out Of Range")

        for i in range(self.__count -1 , index -1, -1):
            self.__arr[i + 1] = self.__arr[i]


        self.__arr[index] = eval(self.__dtype)(value)
        self.__count += 1
            
    def delete(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of bounds")
        
        for i in range(index, self.__count -1):
            self.__arr[i] = self.__arr[i + 1]
        
        self.__arr[self.__count -1] = self.__default_value
        self.__count -=1
    
    def merge(self, merge_arr):
        if not isinstance(merge_arr, Array):
            raise TypeError("must merge Array with another Array.")
        new_size = self.__size + len(merge_arr)
        new_arr = np.empty(new_size, dtype=self.__dtype)
        
        new_arr[:self.__count] = self.__arr[:self.__count]
        new_arr[self.__count:] = merge_arr.__arr[:merge_arr.__count]

        self.__arr = new_arr
        self.__size = new_size
        self.__count += len(merge_arr)

    def is_found(self, element):
        for i in range(self.__count):
            if self.__arr[i] == element:
                return True
        return False        

    def search(self, key):
        index = -1
        for i, n in enumerate(self.__arr[:self.__count]):
            if n == key:
                index = i 
        return index    
    
    def peek(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of range")
        return self.__arr[index]

    
    def length(self):
        return self.__count

    def size(self):
        return self.__size                        

    def display(self):
        if self.is_empty():
            return []
        return self.__arr[:self.__count].tolist()     

    def is_empty(self):
        return self.__count == 0
    

    def sort(self, reverse=False):
        self.__arr[:self.__count] = sorted(self.__arr[:self.__count], reverse=reverse)
        

    def is_sorted(self):
        for i in range(self.__count - 1):
            if self.__arr[i] > self.__arr[i + 1]:
                return False
        return True
    
    def reverse(self):
        self.__arr[:self.__count] = self.__arr[:self.__count][::-1]






if __name__ == "__main__":
    arr = Array(5)
    arr.fill(5, [1,2,3,4,5])
    arr.delete(3)
    print(arr.display())

