# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        
        def dfs(node):
            #baseCase
            if node is None:
                newNode = TreeNode(val)
                return newNode
            
            #recursive cases
            
            if val < node.val:
            #go left
                newNode = dfs(node.left)
            else:
            #go right
                newNode = dfs(node.right)
                
            if not newNode:
                return None
            
            if val > node.val:
                node.right = newNode
            else:
                node.left = newNode
            
            return None
            
        
        dfs(root)
        
        return root
        
        