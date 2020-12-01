# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if(head is None):
            return None
        

        
        curr = head
        c = 0
        while(curr):
            c+= 1
            prev = curr
            curr = curr.next
        

            
        # print(c)
        k = k % c
        
        if(k == 0):
            return head
        
        f_h = c - k
        s_h = c - f_h
        
        # print(f_h,s_h,curr,prev)
        
        curr = head
        
        
        
        while(f_h > 1):
            f_h -= 1
            curr = curr.next
        
        og_head = curr.next
        
        curr.next = None
        
        prev.next = head
        
        return og_head
        
        