# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> int:
        
        if(root is None):
            return 0
        
        
        def dfs(root,summ):
            
            if(root is None):
                return 0
            res = 0
            
            if(root.val == summ):
                res += 1
            
            res += dfs(root.left,summ - root.val)
            res += dfs(root.right,summ - root.val)
            
            return res
        
        
        return self.pathSum(root.left,summ) + self.pathSum(root.right,summ) + dfs(root,summ)