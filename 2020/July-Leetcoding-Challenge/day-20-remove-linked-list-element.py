# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        curr = head
        nullNode = ListNode()
        nullNode.next = head
        prev = nullNode
        head = prev

        # print(head)
        
        while(curr):
            if(curr.val == val):
                # print('equal',curr)
                prev.next = curr.next
                curr = curr.next
                # print(prev,head)
            
            else:
                prev = curr
                curr = curr.next
        
    
        
        return head.next