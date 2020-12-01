# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        c = 0
        
        stack = [root]
        
        if(root is None):
            return 0
        
        while(stack):
            
            p = stack.pop(0)
            
            c += 1
            # print(p)
            
            if(p.left is not None):
                stack.append(p.left)
            
            if(p.right is not None):
                stack.append(p.right)
        
        return c
        
        