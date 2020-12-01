# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if(head is None or head.next is None):
            return head
     
        slow  = head
        fast = head.next
        
        first_even = fast
        
        while(fast and fast.next):
            
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            fast = fast.next
        
        slow.next = first_even
        
        
        return head