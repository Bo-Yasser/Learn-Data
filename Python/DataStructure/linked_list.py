class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def __str__(self):
            return " -> ".join(str(value) for value in self) + " -> None"

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
    
    def __contains__(self, value):
        return self.is_found(value)

    def is_empty(self):
        return self.__count == 0
    
    def is_found(self, value):
        current = self.__head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
    
    def display(self):
        return list(self)

    def insert_last(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            self.__count += 1
            return

        current = self.__head
        while current.next:
            current = current.next
        current.next = new_node
        self.__count += 1    
    
    def insert_first(self, value):
        new_node = Node(value)
        if self.__head:
            new_node.next = self.__head
        
        self.__head = new_node 
        self.__count += 1
    
    def insert_after(self, node_value, value):
        current = self.__head
        if self.__head:
            while current:    
                if current.value == node_value:   
                    new_node = Node(value)
                    new_node.next = current.next 
                    current.next = new_node
                    self.__count += 1
                    return
                current  = current.next
        raise ValueError(f"Value {node_value} not found in the list")
    
    def insert_before(self, node_value, value):
        if self.is_empty():
            raise ValueError("The List Is Empty!")
        
        if self.__head.value == node_value:
            self.insert_first(value)
            return
        
        current = self.__head
        while current.next and current.next.value != node_value:    
            current  = current.next

        if not current.next:
            raise ValueError(f"Value {node_value} not found in the list")
        new_node = Node(value)
        new_node.next = current.next 
        current.next = new_node
        self.__count += 1

    def insert_at_position(self, value, position):
        if position > self.__count + 1 or position < 1:
            raise ValueError("Position Out Of Bounds")    
        
        if position == 1:
            self.insert_first(value)
            return

        new_node = Node(value)
        current = self.__head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node
        self.__count += 1
    
    def get_tail(self):
        if self.is_empty():
            raise ValueError("The List Is Empty!")
        current = self.__head
        while current.next:
            current = current.next
        return current.value
   
    
    def replace(self, node_value, value):
        if self.is_empty():
            raise ValueError("The List Is Empty!")
        
        current = self.__head
        while current:
            if current.value == node_value:
                current.value = value
                return
            current = current.next
        
        raise ValueError(f"Value {node_value} not found in the list")

    def remove(self, value):
        if self.is_empty():
            raise ValueError("List is Empty")
    
        if self.__head.value == value:
            self.__head = self.__head.next
            self.__count -= 1
            return
        
        current = self.__head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.__count -= 1
                return
            current = current.next
        raise ValueError(f"Value {value} Not Found In The List.")
    
    def remove_at_position(self, position):
        if position < 1 or position > self.__count:
            raise IndexError("Position out of range.")
        
        if self.is_empty():
            raise ValueError("List is Empty")
        
        if position == 1:
            self.remove_first()
            return
        
        current = self.__head
        for i in range(position - 2):
            current = current.next
        current.next = current.next.next
        self.__count -= 1

    def remove_first(self):
        if self.is_empty():
            raise ValueError("List is Empty")
        
        self.__head = self.__head.next
        self.__count -= 1

    def remove_last(self):
        if self.is_empty():
            raise ValueError("List is Empty")
        if self.__count == 1:
            self.__head = None
            self.__count -= 1
            return
        current = self.__head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        self.__count -= 1
    
    def remove_all_after(self, element):
        
        current = self.__head
        removed_elements = []
        while current:
            if current.value == element:
                if current.next:

                    removed_count = 0
                    temp = current.next
                    while temp:
                        removed_count += 1
                        removed_elements.append(temp.value)
                        temp = temp.next
                    self.__count -= removed_count
                
                current.next = None
                return removed_elements
            
            current = current.next
        raise ValueError(f"Element {element} not found in the list")
        
    def count(self):
        return self.__count

    def clear(self):
        self.__head = None
        self.__count = 0

    def search(self, element):
        if self.is_empty():
            raise ValueError("List is Empty")
        current = self.__head
        count = 0 
        while current:
            if current.value == element:
                return count
            count += 1
            current = current.next
        return -1 


    def peek(self, index):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if index >= self.__count or index < 0:
            raise IndexError("Index Out Of Range.")
        
        current = self.__head
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise IndexError("element not found.")

    def merge(self, other_list):
        if not isinstance(other_list, LinkedList):
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

    def reverse(self):
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev


if __name__ == "__main__":
    link = LinkedList()

    print(link.is_empty())

    link.insert_last(10)
    link.insert_last(20)
    link.insert_last(30)


    link.insert_first(40)


    link.insert_before(30,70)

    link.insert_at_position(50, 3)

    # link.remove(30)
    # link.replace(40, 11)
    # link.clear()
    print(link.remove_all_after(10))
    print(link.display())
    print(link.count())
    # link.reverse()
    # print(link)
    print(link.get_tail())
    print(link.is_empty())

    # print(link.is_found(50))

    # for i in link:
    #     print(i, end="-")
    # if 50 in link:
    #     print("\na4ta")