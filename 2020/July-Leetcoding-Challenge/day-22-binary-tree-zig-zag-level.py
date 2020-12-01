# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        from collections import deque
        
        
        if(root is None):
            return None
        
        stack = deque([root])
        
        levels = []
        
        while(stack):
            
            c = len(stack)
            # print(stack)
            
            levels.append(list(node.val for node in stack))
            if(len(levels)%2 == 0):
                levels[-1] = levels[-1][::-1]
            # print(c)
            
            while(c > 0):
                
                p = stack.popleft()
                
                
                if(p.left):
                    stack.append(p.left)
                
                if(p.right):
                    stack.append(p.right)
                
                c -= 1
        
        return(levels)
                
            