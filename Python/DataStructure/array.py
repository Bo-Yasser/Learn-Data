# Array Class

import numpy as np
class Array:

    def __init__(self, size, type="int"):
        self.__type = type
        self.__size = size
        self.__arr = np.empty(self.__size, dtype=self.__type)
        self.__count = 0


    def arr_resize(self, new_size):

        if new_size <= self.__size:
            print("New size must be greater than the current size.")
            return
        new_arr = np.empty(new_size, dtype=self.__type)

        for i in range(self.__count):
            new_arr[i] = self.__arr[i]
        
        self.__arr = new_arr
        self.__size = new_size           

    def arr_fill(self, num_elements, elements):

        if num_elements + self.__count > self.__size:
            raise OverflowError("Number of Elements exceeds Array Size!")

        for x, value in enumerate(elements):
            if x >= num_elements: 
                break
            self.__arr[self.__count + x] = eval(self.__type)(value)

        self.__count += num_elements

    def arr_append(self, value):
        if self.__arr is None:
            raise ValueError("Array not initialized. Please create the array first.")
        
        if self.__count < self.__size:
            self.__arr[self.__count] = eval(self.__type)(value)
            self.__count +=1

        else:
            raise OverflowError("Array Is Full!")    
           
    def arr_insert(self, index, value):

        if self.__count >= self.__size:
            raise OverflowError("Array is full. Cannot insert.")
        if index > self.__size:
            raise OverflowError("Index Out Of Range")

        for i in range(self.__count -1 , index -1, -1):
            self.__arr[i + 1] = self.__arr[i]


        self.__arr[index] = eval(self.__type)(value)
        self.__count += 1
            
    def arr_delete(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of bounds")
        
        for i in range(index, self.__count -1):
            self.__arr[i] = self.__arr[i + 1]
        
        self.__arr[self.__count -1] = eval(self.__type)(0)
        self.__count -=1
    
    def arr_merge(self, merge_arr):
        
        new_size = self.__count + len(merge_arr)
        new_arr = np.empty(new_size, dtype=self.__type)
        
        new_arr[:self.__count] = self.__arr[:self.__count]

        new_arr[self.__count:] = merge_arr

        self.__arr = new_arr
        self.__size = new_size
        self.__count = new_size

        

    def arr_search(self, key):
        index = -1
        for i, n in enumerate(self.__arr[:self.__count]):
            if n == key:
                index = i 

        return index    
    
    def arr_length(self):
        return self.__count

    def arr_size(self):
        return self.__size                        

    def arr_display(self):
        return self.__arr[:self.__count]        








if __name__ == "__main__":
    array_size = int(input("Enter the size of the array: "))
    
    arr = Array(array_size)
    

    num_elements = int(input("Enter the number of elements to fill in the array: "))
    elements = []
    
    for i in range(num_elements):
        while True:
            try:
                element = int(input(f"Enter element {i + 1}: "))
            
                elements.append(eval(arr._Array__type)(element)) 
                break  
            except ValueError:
                print(f"Invalid input. Please enter a valid {arr._Array__type} value.")
    
    arr.arr_fill(num_elements, elements)
    print("Array content:", arr.arr_display())
    # append_one_element = eval(arr._Array__type)(input("Enter Just One Element to Add in last index: ")) 
    # arr.arr_append(append_one_element)
    # print("Array content:", arr.arr_display())

    arr.arr_merge([1, 2, 3])
    print("Array content:", arr.arr_display())
    print("Length of elements:", arr.arr_length())
    print("New size:", arr.arr_size())

    # insert_value = eval(arr._Array__type)(input("Enter Just One Element: "))
    # insert_index = int(input("Enter the index: "))
    # arr.arr_insert(insert_index, insert_value)
    # print("Array content:", arr.arr_display())


    # delete_one_element = eval(arr._Array__type)(input("Enter One Element to delete: "))
    # arr.arr_delete(delete_one_element)
    # print("Array content:", arr.arr_display())
    # print("Array size:", arr.arr_size())

    # new_size = int(input("Enter The new Size: "))
    # arr.arr_resize(new_size)
    # print("Array content:", arr.arr_display())
    # print("New size:", arr.arr_size())
    # print("Length of elements:", arr.arr_length())
    
    # ser = int(input("Enter the key: "))

    # result = arr.arr_search(ser)
    # if result != -1:
    #     print(f"Element found at index {result}")
    # else:
    #     print("Element not found")
