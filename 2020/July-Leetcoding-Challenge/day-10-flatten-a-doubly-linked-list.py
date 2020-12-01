"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        stack = [None]
        
        curr = head
        
        if(curr is None):
            return curr
        
        while(curr):
            
            if(curr.child):
                stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            
            if( not curr.next):
                p = stack.pop()
                
                curr.next = p
                
                if(p):
                    p.prev = curr
            
            
            
            curr = curr.next
        
        return head
        


            
            