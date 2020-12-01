# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        ans = 0
        level = [(root,1)]
        
        while level:
            
            next_level = []
            
            ans = max(ans,level[-1][1] - level[0][1] + 1)
            # print(level)
            
            for node,position in level:
                
                if(node.left):
                    next_level.append((node.left,position * 2))
                
                if(node.right):
                    next_level.append((node.right,position*2 + 1))
            
            level = next_level
        
        return ans