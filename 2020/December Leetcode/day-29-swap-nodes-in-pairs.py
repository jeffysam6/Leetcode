# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        
        if(head is None):
            return head
        
        
        rest = ListNode(0)
        rest.next = head
        
        root = rest
        
        
        while(rest.next and rest.next.next):
            
            f = rest.next
            s = rest.next.next
            
            rest.next = s
            temp = s.next
            s.next = f
            f.next = temp
            
            rest = f
            
        
        return root.next
        
        