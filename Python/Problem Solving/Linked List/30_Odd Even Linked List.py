# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return
        
        if not head or not head.next or not head.next.next:
            return head
        
        
        even_head = head.next
        even_tail = even_head
        odd_head= head
        odd_tail = odd_head
        
        curr = even_tail.next
        count = 3
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

        return odd_head
    
    
    
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        odd_head = head
        even_head = head.next
        odd_tail = odd_head
        even_tail = even_head
        curr = even_tail.next
        is_odd = True
        
        while curr:
            if is_odd:
                odd_tail.next = curr
                odd_tail = curr
            else:
                even_tail.next = curr
                even_tail = curr
            curr = curr.next
            is_odd = not is_odd
        
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head
