# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        c = 0
        ans = -1
        
        def inorder(root):
            nonlocal c,ans
            if(root):
                inorder(root.left)
                c += 1
                if(c == k):
                    ans = root.val
                    return

                inorder(root.right)
                
            
        inorder(root)
        
        return ans
        
        