# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        current_path = ""
        def dfs(curr_node, path):
            if not curr_node:
                return
            path = path + str(curr_node.val)
            if not curr_node.left and not curr_node.right:
                all_paths.append(path)
            else:
                path = path + '->'
            dfs(curr_node.left,path)
            dfs(curr_node.right,path)
            return
        dfs(root, current_path)
        return all_paths
                
                
                
                
                
    
    
#             1
#         /.    \ 
#        2. "1->"    3"1->"
#         \
#          5
#     "1->2->5"
        
        
        