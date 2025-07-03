# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # O(n) space complexity and O(n) time complexity
    def pairSum(self, head):
        if not head:
            return
        
        if head and head.next and not head.next.next:
            return head.val + head.next.val

        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next 

        n = len(l)
        pair = float("-inf")
        for i in range(len(l) // 2):
            twin_sum = l[i] + l[n - 1 - i]
            if twin_sum > pair:
                pair = twin_sum

        return pair
    
    
    # O(1) space complexity and O(n) time complexity
    def pairSum(self, head):
        if not head:
            return
        
        if head and head.next and not head.next.next:
            return head.val + head.next.val

        # get the mid element of list to split the list
        fast = head
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
        first = head
        second = prev
        pair = float("-inf")
        while second:
            twin_sum = int(first.val) + int(second.val)
            if twin_sum > pair:
                pair = twin_sum

            first = first.next
            second = second.next
        
        return pair