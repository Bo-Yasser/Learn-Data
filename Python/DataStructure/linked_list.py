class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head == None
    
    def is_found(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
    
    def display(self):
        if self.is_empty():
            print("The list Is Empty")
            return
        current = self.head
        while current:
            print(current.value, end=" ->  ")
            current = current.next
        print("None")
    
    def insert_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node    
    
    def insert_first(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        
        self.head = new_node 
    
    def insert_after(self, node_value, value):
        current = self.head
        if self.head:
            while current:    
                if current.value == node_value:   
                    new_node = Node(value)
                    new_node.next = current.next 
                    current.next = new_node
                    return
                current  = current.next
        raise ValueError(f"Value {node_value} not found in the list")
    
    def insert_before(self, node_value, value):
        if self.is_empty():
            raise ValueError("The List Is Empty!")
        
        if self.head.value == node_value:
            self.insert_first(value)
            return
        
        current = self.head
        while current.next and current.next.value != node_value:    
            current  = current.next

        if not current.next:
            raise ValueError(f"Value {node_value} not found in the list")
        new_node = Node(value)
        new_node.next = current.next 
        current.next = new_node

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:
            self.insert_first(value)
            return

        if position > self.count() or position < 0:
            raise ValueError("Position Out Of Bounds")    
        

        current = self.head
        count = 0
        while current and count < position -1:
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node

    def replace(self, node_value, value):
        if self.is_empty():
            raise ValueError("The List Is Empty!")
        
        current = self.head
        while current:
            if current.value == node_value:
                current.value = value
                return
            current = current.next
        
        raise ValueError(f"Value {node_value} not found in the list")

    def delete(self, value):
        if self.is_empty():
            raise ValueError("List is Empty")
    
        if self.head.value == value:
            self.head = self.head.next
            print(f"Value {value} deleted successfully.")
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                print(f"Value {value} deleted successfully.")
                return
            current = current.next
        raise ValueError(f"Value {value} Not Found In The List.")
    
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
    
 
            
if __name__ == "__main__":
    link = LinkedList()

    print(link.is_empty())

    link.insert_last(10)
    link.insert_last(20)
    link.insert_last(30)


    link.insert_first(40)


    link.insert_before(30,70)

    link.insert_at_position(50, 5)

    # link.delete(30)
    link.replace(40, 11)
    # link.clear()
    link.display()
    print(link.count())

    # print(link.is_empty())

    # print(link.is_found(50))