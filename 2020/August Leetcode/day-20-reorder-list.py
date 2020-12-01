# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if(head is None or head.next is None ):
            return
        
        arr = []
        
        curr = head
        while(curr):
            arr.append(curr)
            curr = curr.next
        
        mid = len(arr)//2
        
        
        l = 0
        curr = head
        while(curr):
            
            if(len(arr) %2 ==0 and l == mid-1):
                curr.next = None
                
            elif(len(arr) %2 !=0 and l == mid):
                curr.next = None
            curr = curr.next
            l += 1

                
        # print(head)
            
        arr = arr[mid:][::-1]
        
        
        # print(arr,mid)
        
        arr_ptr = 0
        
        curr = head
        
        # print(arr,curr.val)
        while(curr  and arr_ptr < len(arr)):
            forward = curr.next
            curr.next = arr[arr_ptr]
            
            curr.next.next = forward
            arr_ptr += 1
            
            if(curr.next and curr.next.next):
                prev = curr.next
                curr = curr.next.next
                
            else:
                return
        
        if(arr_ptr < len(arr)):
            prev.next = arr[arr_ptr]
            prev.next.next = None
        # print(prev)

        
            