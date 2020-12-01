
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:


        levels = {}
        
        
        def level_traverse(node,parent,level):
            if(not node):
                return 
            
            levels[level] = levels.get(level,{})
            
            levels[level].update({node.val:parent})
            
            level_traverse(node.left,node.val,level+1)
            
            level_traverse(node.right,node.val,level+1)
            
        level_traverse(root,None,0)
        
        for i in levels:
            
            if(x in levels[i] and y in levels[i]):
                
                if(levels[i][x] != levels[i][y]):
                    return True
        
        return False
                
