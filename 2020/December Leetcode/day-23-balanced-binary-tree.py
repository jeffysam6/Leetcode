# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if(root is None):
            return True
        
        
        def diff(root):
            
            if(root is None):
                return 0 , True
            
            lh,lb = diff(root.left)
            rh,rb = diff(root.right)
            
            return max(lh,rh)+1 , abs(lh - rh) <= 1 and lb and rb
        
        
        return diff(root)[1]
    