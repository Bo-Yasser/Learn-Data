class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0
    
    def __str__(self):
        return f"Queue: {list(self)}"

    def __iter__(self):
        current = self.__front
        while current:
            yield current.value
            current = current.next
    
    def __contains__(self, value):
        return self.is_found(value)
    
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.__front = self.__rear = new_node
            
        else:
            self.__rear.next = new_node
            self.__rear = new_node
        self.__count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        dequeue_value = self.__front.value
        self.__front = self.__front.next
        
        if not self.__front:
            self.__rear = None

        self.__count -= 1
        return dequeue_value
    

    def display(self):
        return list(self)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.__front.value
    
    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.__rear.value
    
    def is_empty(self):
        return self.__count == 0
    
    def is_found(self, element):
        current = self.__front
        while current:
            if current.value == element:
                return True
            current = current.next
        return False
    
    def search(self, element):
        current = self.__front
        count = 0 
        while current:
            if current.value == element:
                return count
            count += 1
            current = current.next
        raise ValueError("element not found.")
    
    def count(self):
        return self.__count
    
    def clear(self):
        self.__front = None
        self.__rear = None
        self.__count = 0
    
    def sort(self, reverse=False):
        values = list(self)
        values.sort(reverse=reverse)
        self.clear()
        for value in values:
            self.enqueue(value)
    
    def is_sorted(self):
        current = self.__front
        while current and current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True

    def reverse(self):
        current = self.__front 
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__rear, self.__front = self.__front, self.__rear

    def merge(self, other_queue):
        if not isinstance(other_queue, LinkedQueue):
            raise TypeError("must merge Queue with another Queue.")
        for value in list(other_queue):
            self.enqueue(value)

if __name__ == "__main__":
    link = LinkedQueue()

    link.enqueue(10)
    link.enqueue(20)
    link.enqueue(30)
    link.enqueue(40)
    link.enqueue(50)

    link.dequeue()

    print(link.display())
    print(link.search(20))
    print(link.is_found(10))
    print(link.front())
    print(link.rear())

    print("#"* 50)
    link.reverse()
    print(link.display())
    print(link.search(20))
    print(link.is_found(20))
    print(link.front())
    print(link.rear())

    print("#"* 50)
    link.clear()
    print(link.display())

