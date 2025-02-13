class Node:
    def __init__(self, value):
        
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
        
    def __str__(self):
        return f"{list(self)}"
    
    def __contains__(self, value):
        return self.is_found(value)

    def is_empty(self):
        return self.__count == 0    
    
    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__count += 1
            return
        
        new_node.next = self.__head
        self.__head.prev = new_node 
        self.__head = new_node
        self.__count += 1 

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.__head = self.__tail = new_node
            self.__count += 1
            return
        
        new_node.prev = self.__tail
        self.__tail.next = new_node
        self.__tail = new_node
        self.__count += 1

    def insert_at_pos(self, pos, value):
        if pos < 0 or pos > self.__count:
            raise IndexError("Out of range!")
        else:
            if pos == 0:
                self.insert_first(value)
                return
            
            elif pos == self.__count:
                self.insert_last(value)
                return
            else:
                new_node = Node(value)
                current = self.__head
                for i in range(1, pos):
                    current = current.next
        
                # 2
                # count = 1
                # current = self.__head.next
                # while current.next:
                #     if count == pos - 1:
                #         break
                #     current = current.next
                #     count += 1
        
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                self.__count += 1

    def insert_after(self, value, new_value):
        if self.is_empty():
            raise IndexError("List is empty! nothing to insert after.")
        
        if self.__tail.value == value or self.__count == 1:
            self.insert_last(new_value)
            return
        
        new_node = Node(new_value)
        if self.__head.value == value:
            new_node.next = self.__head.next
            new_node.prev = self.__head
            self.__head.next.prev = new_node
            self.__head.next = new_node
            self.__count += 1
            return
        
        if self.__tail.prev.value == value:
            new_node.next = self.__tail
            new_node.prev = self.__tail.prev
            self.__tail.prev.next = new_node
            self.__tail.prev = new_node
            self.__count += 1
            return
        
        current = self.__head
        while current and current.value != value:
            current = current.next
        
        if current is None:
            raise ValueError(f"Value {value} not found in the list")
        
        new_node.next = current.next
        new_node.prev = current 
        current.next.prev = new_node
        current.next = new_node 
        self.__count += 1
    
    def insert_before(self, value, new_value):
        if self.is_empty():
            raise IndexError("List is empty! nothing to insert before.")
        
        if self.__head.value == value or self.__count == 1:
                self.insert_first(new_value)
                return
  
        new_node = Node(new_value)
        if self.__tail.value == value:
            new_node.next = self.__tail
            new_node.prev = self.__tail.prev
            self.__tail.prev.next = new_node
            self.__tail.prev = new_node
            self.__count += 1
            return
        
        current = self.__head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next is None:
            raise ValueError(f"Value {value} not found in the list")
        
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.__count += 1

    def insert_no_duplicate(self, value):  
        if self.search(value) == -1:
            self.insert_last(value)
        else:
            print("Element already in Array.")
        
    def fill(self, values):
        if not values:
            raise ValueError("Invalid type.")
        for value in values:
            self.insert_last(value)

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        poped_value = self.__head.value
        
        if self.__count == 1:
            self.__head = self.__tail = None

        else:
            self.__head = self.__head.next
            self.__head.prev = None
        
        self.__count -= 1
        return poped_value
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 1:
            return self.remove_first()
        
        poped_value = self.__tail.value
        self.__tail = self.__tail.prev
        self.__tail.next = None
        self.__count -= 1
        return poped_value

    def remove_at_pos(self, pos):
        if self.is_empty():
            raise IndexError("List is empty.")
        if pos < 0 or pos > self.__count:
            raise IndexError("Out of range!")
        else:
            if pos == 0:
                return self.remove_first()

            elif pos == self.__count - 1:
                return self.remove_last()

            else:
                current = self.__head
                for i in range(pos):
                    current = current.next
                poped_value = current.value
                current.next.prev = current.prev
                current.prev.next = current.next
                self.__count -= 1
                return poped_value
    
    def remove_after(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")

        if self.__count == 1 or self.__tail.value == value :
            raise IndexError(f"Out of range! nothing after {value}.")

        if self.__tail.prev.value == value:
            return self.remove_last()
        
        
        else:
            current = self.__head
            while current and current.next:
                if current.value == value:
                    break
                current = current.next

            poped_value = current.next.value
            current.next.next.prev = current
            current.next = current.next.next
            self.__count -= 1
            return poped_value

    def remove_before(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")

        if self.__count == 1 or self.__head.value == value :
            raise IndexError(f"Out of range! nothing before {value}.")
        
        if self.__head.next and self.__head.next.value == value:
            return self.remove_first()
        
        current = self.__head
        while current and current.next.value != value:
            current = current.next
        
        poped_value = current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        self.__count -= 1
        return poped_value
        
    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("List is empty.")

        elif self.__head.value == value:
            return self.remove_first()

        elif value is None or self.__tail.value == value:
            return self.remove_last()

        else:
            current = self.__head.next
            while current.next and current.value != value:
                current = current.next
            if current == self.__tail:
                raise ValueError(f"Element {value} not found in list")

            poped_value = current.value
            current.next.prev = current.prev
            current.prev.next = current.next   
            self.__count -= 1
            return poped_value

    def remove_all_before(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 1 or self.__head.value == value :
            raise IndexError(f"Out of range! nothing before {value}.")        
        
        l = []
        count = self.search(value)
        for i in range(count - 1):
            l.append(self.remove_before(value))
        return l
    
    def remove_all_after(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 1 or self.__tail.value == value :
            raise IndexError(f"Out of range! nothing after {value}.")        
        
        l = []
        count = self.search(value)
        for i in range(self.__count - count):
            l.append(self.remove_after(value))
        return l
    
    def display(self, reverse=False):
        if self.is_empty():
            return []
        
        l = []
        if reverse is False: 
            current = self.__head
            while current:
                l.append(current.value)
                current = current.next
            return l
        
        rev_current = self.__tail
        while rev_current:
            l.append(rev_current.value)
            rev_current = rev_current.prev
        return l        
    
    def get_head(self):
        return self.__head.value
    
    def get_tail(self):
        return self.__tail.value

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_found(self, value):
        if self.search(value) == -1:
            return False
        
        return True
    
    def search(self, value):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        elif value == self.__head.value:
            return 0

        elif value == self.__tail.value:
            return self.__count - 1        
        
        current = self.__head
        count = 0
        while current.next:
            if current.value == value:
                return count
            count += 1
            current = current.next
        
        return -1
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
        while current.next:
            if count == index:
                return current.value
            
            count += 1
            current = current.next

    def merge(self, other_list):
        if not isinstance(other_list, DoublyLinkedList):
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
        while current and current.next:
            if current.value > current.next.value:
                return False
            current = current.next
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

        while current.next:
            if current.value == value:
                current.value = new_value
                return
            current = current.next
        raise ValueError(f"element {value} not found in the list")
    
    def reverse(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count <= 1:  
            return
        
        current = self.__head
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node

            current = next_node
        
        self.__head, self.__tail = self.__tail, self.__head





l = DoublyLinkedList()

l.insert_first(2)
l.insert_first(1)
l.insert_last(3)
l.insert_last(4)

l.insert_at_pos(2, 2.5)


# l.remove_last()
# l.remove_at_pos(4)



# print(l.peek())

# l.insert_after(2.5, 5)

l.insert_before(2, 5)

# l.insert_before(1, 80)
# print(l.remove_at_pos(4))

# l.remove_before(80)
# print(l._DoublyLinkedList__tail.prev.value)
# print(l.remove_after(3))

# print(l.remove_before(2))
# print(l.remove_before(2.5))
# print(l.remove_before(3))
# print(l.remove_before(4))

# print(l.search(2.5))

print(l.get_head())
print(l.get_tail())
print(l.display())

l.reverse()

print(l.display())
print(l.get_head())
print(l.get_tail())

# print(len(l))

        
            
