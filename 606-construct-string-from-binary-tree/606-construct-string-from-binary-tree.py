# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def traverse(node, my_str):
            if not node:
                return ""
            
            my_str += str(node.val)  
            
            if not node.left and not node.right:
                return my_str
            
            left_str = traverse(node.left,"")
            right_str = traverse(node.right,"")
            
            if left_str == right_str == "":
                return f"{my_str}"
            if right_str == "":
                 return f"{my_str}({left_str})"
    
            return f"{my_str}({left_str})({right_str})"
            
            
        str_build = traverse(root, "")
        
        return str_build
        
        