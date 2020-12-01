# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if(p and q):
            
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        return p is q


        
#         stack = [(p,q)]
        
#         while(stack):
            
#             pnode,qnode = stack.pop()
            
        
            
#             if(not pnode and not qnode):
#                 continue
            
#             elif(None in [pnode,qnode]):
#                 return False
            
#             else:
#                 if(pnode.val != qnode.val):
#                     return False
#                 stack.append((pnode.left,qnode.left))
#                 stack.append((pnode.right,qnode.right))
                
        
#         return True
                
            
            