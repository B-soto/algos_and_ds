# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [(root,0)]
        return_list = []
        seen_level = {0}
        this_level = []
        
        while q:
            curr, depth = q.pop(0)
            # data = curr.val
            if depth not in seen_level:
                return_list.append(this_level)
                this_level = [curr.val]
                seen_level.add(depth)
            else:
                this_level.append(curr.val)
            
            if curr.left:
                q.append((curr.left, depth+1))
            if curr.right:
                q.append((curr.right, depth+1))
        
        if this_level: return_list.append(this_level)
        return return_list
                
                
        
        