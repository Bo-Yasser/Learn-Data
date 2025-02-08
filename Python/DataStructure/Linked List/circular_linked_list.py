class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def __len__(self):
        return self.__count
    
    def __str__(self):

        return f"{list(self)}"

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
            if current == self.__head:
                break
        
    def __contains__(self, value):
        return self.is_found(value)

    def is_empty(self):
        return self.__count == 0
    
    def insert_first(self, value):
        new_node = Node(value)

        if self.__count == 0:
            self.__head = self.__tail = new_node
            self.__tail.next = self.__head
            
        else:
            self.__tail.next = new_node
            new_node.next = self.__head
            self.__head = new_node

        self.__count += 1

    def insert_last(self, value):
        new_node = Node(value)

        if self.__count == 0:
            self.__head = self.__tail = new_node
            self.__tail.next = self.__head
            
        else:
            self.__tail.next = new_node 
            self.__tail = new_node
            self.__tail.next = self.__head

        self.__count += 1

    def insert_at_pos(self, pos, value):
        new_node = Node(value)

        if pos > self.__count or pos < 0:
            raise OverflowError(f"Index out of range.")
        else:
            if pos == self.__count:
                self.insert_last(value)
                return
            
            elif pos == 0:
                self.insert_first(value)
                return
            else:
                current = self.__head
                for i in range(1, pos):
                    current = current.next
                
                new_node.next = current.next
                current.next = new_node
                self.__count += 1 
    
    def insert_before(self, value, new_value):
        
        
        if self.__count == 0 or self.__head.value == value:
                self.insert_first(new_value)
                return
        
        new_node = Node(new_value)
        current = self.__head
        while current.next != self.__tail and current.next.value != value:
            current = current.next
        
        if current.next.value != value:
            raise ValueError(f"Value {value} not found in the list")
        new_node.next = current.next
        current.next = new_node
        self.__count += 1

    def insert_after(self, value, new_value):
        if self.__count == 0:
                self.insert_first(new_value)
                return
        
        elif self.__tail.value == value:
            self.insert_last(new_value)
            return
        
        new_node = Node(new_value)
        current = self.__head
        while current.next != self.__tail:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                self.__count += 1
                return
            current = current.next
        raise ValueError(f"Value {value} not found in the list")
    
    def fill(self, values):
        if not values:
            raise ValueError("Invalid type.")
        for value in values:
            self.insert_last(value)

    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if value is None or self.__tail.value == value:
            return self.remove_last()

        
        if self.__head.value == value:
            return self.remove_first()


        current = self.__head.next
        prev = self.__head
        while current.next != self.__tail and current.value != value:
            prev = current
            current = current.next

        if current.value != value:
            raise ValueError(f"Value {value} not found in list.")
        prev.next = current.next
        self.__count -= 1
        return current.value

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        poped_value = self.__head.value
        
        if self.__count == 1:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__tail.next = self.__head
        
        self.__count -= 1
        return poped_value

    def remove_last(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 1:
            return self.remove_first()

        
        current = self.__head
        prev = None
        while current.next != self.__head:
            prev = current
            current = current.next
        poped_value = current.value
        prev.next = self.__head
        self.__tail = prev
        self.__count -= 1
        return poped_value
    
    def remove_at_position(self, index):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if index < 0 or index > self.__count -1:
            raise IndexError("Out of range.")
        
        if index == 0:
            return self.remove_first()

        
        if index == self.__count - 1:
            return self.remove_last()

        
        
        current = self.__head
        for i in range(index - 1):
            current = current.next
        poped_value = current.next.value
        current.next = current.next.next
        self.__count -= 1
        return poped_value

    def remove_after(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 1 or self.__tail.value == value :
            raise IndexError(f"Out of range! nothing before {value}.")
        

        current = self.__head
        while current.next != self.__tail and current.value != value:
                current = current.next

        if current.next == self.__tail:
            poped_value = self.__tail.value
            self.__tail = current
            self.__tail.next = self.__head
            self.__count -= 1
            return poped_value
        
        poped_value = current.next.value
        current.next = current.next.next
        self.__count -= 1
        return poped_value

    def remove_before(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__head.value == value:
            raise OverflowError(f"Out of range! nothing before {value}.")
        
        if self.__head.next and self.__head.next.value == value:
            poped_value = self.__head.value
            self.__head = self.__head.next
            self.__tail.next = self.__head
            self.__count -= 1
            if self.__count == 1:
                self.__tail = self.__head
            return poped_value
        
        current = self.__head.next
        prev = self.__head
        while current.next != self.__tail and current.next.value != value:
            prev = current
            current = current.next
        
        if current.next.value != value:
            raise ValueError(f"Value {value} not found in list.")
        
        poped_value = current.value
        prev.next = current.next
        self.__count -= 1
        return poped_value

    def remove_all_after(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")

        if self.__tail.value == value:
            raise IndexError("No elements after the given value.")

        current = self.__head
        while current != self.__tail:
            if current.value == value:
                count = 0
                temp = current.next
                while temp != self.__head:  
                    temp = temp.next
                    count += 1

                self.__tail = current 
                current.next = self.__head  
                self.__count -= count
                return
            current = current.next

        raise ValueError(f"Element {value} not found in the list.")

    def remove_all_before(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")

        if self.__head.value == value:
            raise IndexError("No elements before the given value.")

        current = self.__head
        count = 0
        while current.next != self.__head:
            count += 1  
            if current.next.value == value:
                self.__head = current.next
                self.__tail.next = self.__head
                self.__count -= count 
                return
            current = current.next

        raise ValueError(f"Element {value} not found in the list.")
    
    def display(self):
        return list(self)
    
    def get_head(self):
        return self.__head.value
    
    def get_tail(self):
        return self.__tail.value
    
    def clear(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def peek(self, index):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        elif index > self.__count - 1 or index < 0:
            raise OverflowError(f"Index out of range.")       
        
        elif index == 0:
            return self.__head.value
        
        elif index == self.__count - 1:
            return self.__tail.value
        
        current = self.__head.next
        count = 1
        while current.next != self.__head:
            if count == index:
                return current.value
            
            count += 1
            current = current.next

    def search(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        elif value == self.__head.value:
            return 0

        elif value == self.__tail.value:
            return self.__count - 1
        
        current = self.__head.next
        count = 1
        while current != self.__head:
            if current.value == value:
                return count
            count += 1
            current = current.next
        return -1
    
    def is_found(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        elif self.search(value) == -1:
            return False
        
        return True
    
    def replace(self, value, new_value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        elif self.__head.value == value:
            self.__head.value = new_value
            return

        elif self.__tail.value == value:
            self.__tail.value = new_value
            return
        
        current = self.__head.next
        while current != self.__head:
            if current.value == value:
                current.value = new_value
                return
            current = current.next
        raise ValueError(f"element {value} not found in the list")
    
    def merge(self, other_list):
        if not isinstance(other_list, CircularLinkedList):
            raise TypeError("must merge List with another List.")
        current = other_list.__head
        while current:
            self.insert_last(current.value)
            current = current.next
 
    def sort(self, reverse=False):
        values = list(self)
        values.sort(reverse=reverse)
        self.clear()
        for value in values:
            self.insert_last(value)
    
    def is_sorted(self):
        current = self.__head
        while current != self.__tail:
            if current.value > current.next.value:
                return False
            current = current.next
        return True

    def reverse(self):
        if self.__count <= 1:  
            return
        
        prev = self.__tail
        current = self.__head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if prev == self.__tail:
                break
        self.__tail = self.__head
        self.__head = prev
        self.__tail.next = self.__head  


l = CircularLinkedList()

l.insert_first(1)
l.insert_first(2)

l.insert_last(5)
l.insert_last(4)
l.insert_last(6)

l.remove_before(6)
# l.remove_last()
# l.remove_last()
# l.remove_last()
# l.remove_last()
# l.remove_last()

# l.remove_all_after(4)
# l.remove_all_before(1)
# l.reverse()
# print(l.get_head())
# print(l.get_tail())

# l.pop(7)
print(l)
# print(l.peek(3))
# print(l.search(7))
# print(len(l))