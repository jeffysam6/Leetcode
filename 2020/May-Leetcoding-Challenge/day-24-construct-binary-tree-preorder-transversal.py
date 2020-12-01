# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, arr: List[int]) -> TreeNode:
        
        def insert(root,node):

            if(root):

                if(node.val > root.val):

                    if(root.right):
                        insert(root.right,node)

                    else:
                        root.right = node


                elif(node.val < root.val):

                    if(root.left):
                        insert(root.left,node)

                    else:
                        root.left = node




        root = TreeNode(arr[0])




        for i in range(1,len(arr)):
            insert(root,TreeNode(arr[i]))




        return(root)
