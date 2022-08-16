# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level = 0
        q = [(root,level)]
        return_list = []
        seen_level = {level}
        this_level = []
        
        while q:
            curr, depth = q.pop(0)
            data = curr.val
            if depth not in seen_level:
                return_list.append(this_level)
                this_level = [data]
                seen_level.add(depth)
            else:
                this_level.append(data)
            
            if curr.left:
                q.append((curr.left, depth+1))
            if curr.right:
                q.append((curr.right, depth+1))
        
        if this_level: return_list.append(this_level)
        return return_list
                
                
        
        