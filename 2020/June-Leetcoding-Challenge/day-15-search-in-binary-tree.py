# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        
#         def level(root):
            
#             stack = [root]
#             ans = []
            
#             while(stack):
#                 p = stack.pop(0)
#                 ans.append(p.val)
#                 if(p.left):
#                     stack.append(p.left)
                
#                 if(p.right):
#                     stack.append(p.right)
            
#             # print(ans)
                    
#             return ans
        
        if(root is not None):
            
            if(val == root.val):
                return root
            
            elif(val > root.val):
                return self.searchBST(root.right,val)
                
            
            else:
                return self.searchBST(root.left,val)
                
        else:
            return None
                
        
                
        
      