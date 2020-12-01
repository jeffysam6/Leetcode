# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        
        
        if(root is  None):
            return 0
        stack = [(root,root.val)]
        ans = 0
        
        while(stack):
            node,val = stack.pop(0)
            # print('p',p[-1].left is not None,p[-1].right is not None)
            # print('stack',stack)

            if(node):

                if(not node.left and not node.right):
                    ans += val

                if(node.left):
                    stack.append((node.left,val*10+node.left.val))

                if(node.right):
                    stack.append((node.right,val*10 + node.right.val))
                        
        return ans