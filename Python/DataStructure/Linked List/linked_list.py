class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def __len__(self):
        return self.__count
    
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
    
    def insert_no_duplicate(self, value):  
        if self.search(value) == -1:
            self.insert_last(value)
        else:
            print("Element already in Array.")
    
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
        if self.is_empty():
            raise ValueError("List is Empty")       
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


    def deleteMiddle(self):

        if self.is_empty():
            raise ValueError("List is Empty")
        curr = self.__head
        if self.__count == 1:
            self.__head = None
            self.__count -= 1
            return
           
        prev = None
        for i in range(self.__count // 2):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        self.__count -= 1
        
        
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
    
    def selection_sort(self, reverse=False):
        current = self.__head
        if not reverse:
            for i in range(self.__count - 2):
                minidx = current
                com = current
                for j in range(i + 1, self.__count):
                    if minidx.value > com.next.value:
                        minidx.value, com.next.value = com.next.value, minidx.value
                
                current = current.next

    def is_sorted(self):
        current = self.__head
        while current and current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True

    def reverse(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count <= 1:  
            return
        
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    def oddEvenList(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count < 3:
            return
        
        
        even_head = self.__head.next
        even_tail = even_head
        odd_head= self.__head
        odd_tail = odd_head
        
        curr = even_tail.next
        count = 1
        while curr:

            if count % 2 != 0:
                odd_tail.next = curr
                odd_tail = curr
                
            if count % 2 == 0:
                even_tail.next = curr
                even_tail = curr
            
            
            curr = curr.next
            count += 1
        

        odd_tail.next = even_head
        even_tail.next = None
        self.__head = odd_head

    # O(n) space complexity and O(n) time complexity
    # def pairSum(self):
    #     if self.is_empty():
    #         raise IndexError("List is empty.")
        
    #     if self.__count == 2:
    #         return self.__head.value + self.__head.next.value

    #     curr = self.__head
    #     l = []
    #     while curr:
    #         l.append(curr.value)
    #         curr = curr.next 

    #     n = len(l)
    #     pair = float("-inf")
    #     for i in range(len(l) // 2):
    #         twin_sum = l[i] + l[n - 1 - i]
    #         if twin_sum > pair:
    #             pair = twin_sum

    #     return pair

    # O(1) space complexity and O(n) time complexity
    def pairSum(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        
        if self.__count == 2:
            return self.__head.value + self.__head.next.value

        # get the mid element of list to split the list
        fast = self.__head
        slow = fast 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        # reverse the second half of list 
        # to make each element match his twin or be in the same order or index
        curr = slow
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # sum every twin to get the highest pair sum
        first = self.__head
        second = prev
        pair = float("-inf")
        while second:
            twin_sum = int(first.value) + int(second.value)
            if twin_sum > pair:
                pair = twin_sum

            first = first.next
            second = second.next
        
        return pair

if __name__ == "__main__":
    link = LinkedList()

    # print(link.is_empty())

    link.insert_last(10)
    link.insert_last(20)
    link.insert_last(30)


    link.insert_first(40)

    # link.insert_before(30,70)

    # link.insert_at_position(50, 3)
    # link.selection_sort()
    # link.deleteMiddle()
    # link.oddEvenList()
    
    print(link.display())
    print(link.pairSum())
    # link.remove(30)
    # link.replace(40, 11)
    # link.clear()
    # print(link.remove_all_after(10))
    # print(link.display())
    # print(len(link))
    # link.reverse()
    # print(link)
    # print(link.get_tail())
    # print(link.is_empty())

    # print(link.is_found(50))

    # for i in link:
    #     print(i, end="-")
    # if 50 in link:
    #     print("\na4ta")