# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        queue = [(root, level)]
        total_sum = 0
        seen_level = set()
        while queue:
            curr_node, level = queue.pop(0)
            if level not in seen_level:
                total_sum = 0
                seen_level.add(level)
            total_sum += curr_node.val
            
            if curr_node.left: queue.append((curr_node.left,level+1))
            if curr_node.right: queue.append((curr_node.right,level+1))
            
            
        
        
        return total_sum
        
        
        
        
#     q = [5]
    
#     seen_level = {1,2}
#     total_sum = 5
#     q = []
    
#       1 
#     /   \
#    2     3. curr 3 level 2
    

    
    
    

    
    
    
    
    