import numpy as np

class Queue:

    def __init__(self, size, dtype="int"):
        self.__size = size
        self.__dtype = dtype
        self.__arr = np.empty(self.__size, dtype=self.__dtype)
        self.__default_value = self.__arr[0]
        self.__front = 0
        self.__rear = self.__size - 1
        self.__count = 0
    def __str__(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Queue{self.display()}"
    
    def __iter__(self):
        return iter(self.__arr[:self.__count])
    
    def __contains__(self, value):
        return self.is_found(value)
    
    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("queue is full no space to enqueue.")
        if not np.issubdtype(type(data), np.dtype(self.__dtype).type):
            raise TypeError(f"Invalid type. Please enter a valid {self.__dtype} type.")

        self.__rear = (self.__rear+1)%self.__size  
        self.__arr[self.__rear] = data
        self.__count +=1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        dequeue_value = self.__arr[self.__front]
        self.__arr[self.__front] = self.__default_value
        self.__front = (self.__front + 1)%self.__size
        self.__count -=1 
        return dequeue_value
        
    def is_empty(self):
        return self.__count == 0
    
    def is_full(self):
        return self.__count == self.__size
    
    def is_found(self, element):
        for i in range(self.__count):
            if self.__arr[i] == element:
                return True
        return False
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.__arr[self.__front]
    
    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.__arr[self.__rear]
    
    def search(self, element):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        
        for i in range(self.__count):
            if self.__arr[i] == element:
                return i
        return -1
    
    def peek(self, index):
        if index < 0 or index >= self.__count:
            raise IndexError("Index out of range")
        return self.__arr[index]
    
    def size(self):
        return self.__size

    def resize(self, new_size):
        if new_size <= self.__size:
            raise ValueError("new size must be larger than current size.")
        
       
        new_arr = np.empty(new_size, dtype=self.__dtype)

   
        for i in range(self.__count):
            new_arr[i] = self.__arr[(self.__front + i) % self.__size]

        self.__arr = new_arr
        self.__front = 0
        self.__rear = self.__count - 1
        self.__size = new_size
        
    def count(self):
        return self.__count

    def clear(self):
        self.__arr.fill(self.__default_value)
        self.__front = 0 
        self.__rear = self.__size -1
        self.__count = 0
    
    def merge(self, other_queue):
        if not isinstance(other_queue, Queue):
            raise TypeError("Can only merge with another Queue.")
        
        new_size = self.__count + other_queue.count()
        
        if new_size > self.__size:
            raise OverflowError("Not Enough Space To Merge Stacks.")
    
        for i in range(other_queue.count()):
            self.enqueue(other_queue.peek(i))

    
    def display(self):
        if self.is_empty():
            return []

        return [self.__arr[(self.__front +i)% self.__size].item() for i in range(self.__count)]
        
        # 2
        # l = []
        # for i in range(self.__count):
        #     l.append(self.__arr[(self.__front +i)% self.__size].item())
        #     # 2
        #     # i = (self.__front +i)% self.__size
        #     # l.append(self.__arr[i].item())
        # return l
    
        # 3
        # l = []
        # i = self.__front
        # while i != self.__rear:
        #     l.append(self.__arr[i].item())
        #     i = (i + 1)% self.__size
        # l.append(self.__arr[self.__rear].item())
        # return l
    
    def sort(self, reverse=False):
        self.__arr[:self.__count] = sorted(self.__arr[:self.__count], reverse=reverse)
        self.__front = 0
        self.__rear = self.__count - 1
        

    def is_sorted(self):
        for i in range(self.__count - 1):
            if self.__arr[i] > self.__arr[i + 1]:
                return False
        return True
    
    def reverse(self):
        self.__arr[:self.__count] = self.__arr[:self.__count][::-1]
        self.__front, self.__rear = self.__rear, self.__front

if __name__ == "__main__":
    queue = Queue(5)

    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.dequeue()
    queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()

    queue.enqueue(10)
    # queue.dequeue()

    queue.enqueue(20)
    # queue.enqueue(30)


    print(queue.display())

    # print(queue.is_empty())
    # print(queue.is_full())

    # print(queue.front())
    # print(queue.rear())


    # print(queue.search(30))

    # print(queue.size())
    # queue.resize(7)
    # print(queue.size())


    # print(queue)
    # for i in queue:
    #     print(i, end="-")
    # if 30 in queue:
    #     print("\na4ta")


    # queue2 = Queue(3)
    # queue2.enqueue(40)
    # queue2.enqueue(50)
    # print(queue2)

    # queue.merge(queue2)
    # print(queue)

    # queue.sort()
    # print(queue.display())
    # print(queue.is_sorted())

