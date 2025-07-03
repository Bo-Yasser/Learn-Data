# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def deleteMiddle(self, head):
        curr = head
        count = 0 
        while curr:
            count += 1

s = Solution()


