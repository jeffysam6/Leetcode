# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        from collections import deque
        
        stack = deque([root])
        
        ans = []
        if(root is None):
            return []
        
        while(stack):
            l = len(stack) 
            temp = []
            for i in stack:
                temp.append(i.val)
            ans.append(temp)
            
            while(l > 0):
                p = stack.popleft()
                l -= 1
                if(p.left):
                    stack.append(p.left)
                if(p.right):
                    stack.append(p.right)
                        
                
        
        return reversed(ans)
        
        
