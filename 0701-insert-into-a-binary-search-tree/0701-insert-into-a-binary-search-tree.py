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
        
        
        def dfs(node, parent):
            #baseCase
            if node is None:
                newNode = TreeNode(val)
                
                if val > parent.val:
                    parent.right = newNode
                else:
                    parent.left = newNode
                return
            
            #recursive cases
            parent = node
            
            if val < node.val:
            #go left
            
                dfs(node.left, parent)
            else:
            #go right
                dfs(node.right, parent)
            
            
            return
            
        
        dfs(root,None)
        
        return root
        
        