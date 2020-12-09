# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.nodes = []
        def dfs(root):
            if(root is not None):
                dfs(root.left)
                self.nodes.append(root.val)
                dfs(root.right)
        self.pointer = -1
        dfs(root)
            
    def next(self) -> int:
        self.pointer += 1
        return self.nodes[self.pointer]
        
    def hasNext(self) -> bool:
        return self.pointer+1 < len(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()