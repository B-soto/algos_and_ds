# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        this_level = [(1,root)]
        width = 1
        
        while this_level:
            next_level = []
            level_width = (this_level[-1][0] - this_level[0][0])+1
            width = max(width, level_width)
            
            for position, current_node in this_level:
                if current_node.left:
                    next_level.append([position*2, current_node.left])
                if current_node.right:
                    next_level.append([(position*2) +1, current_node.right])
            
            this_level = next_level
        return width
            
        
#         this_level = [[4, 5node], [5, 3node], [7, 9node]]
#         next_level = []
#         7-4 +1
        
        
        
#                    1  (1, TRUE)
#                 /.    \
#                2(2, 3node)        2+1
#              /  \      / \ 
#             4.   4+1     6+1        
            
            
        
        
        
        
        
        
        
        
        
#         max_width = 1
#         this_level = [root]
#         width = 0
#         while this_level and width > -1:
#             next_level = []
#             for node in this_level:
#                 if node.left:
#                     next_level.append(node.left)
#                 else:
#                     #print('here')
#                     node.left = TreeNode(val= 'x')
#                     next_level.append(node.left)
           
#                 if node.right:
#                     next_level.append(node.right)
#                 else:
#                     #print('here2')
#                     node.right = TreeNode(val= 'x')
#                     next_level.append(node.right)
                    
            
            
#             this_level_values = [n.val for n in this_level]
#             #print(this_level_values)
#             if set(this_level_values) == {'x'}:
#                 break
#             right = len(this_level_values) -1
#             left = 0
#             while type(this_level_values[right]) != int or type(this_level_values[left]) != int:
#                 #print('here', left, right)
#                 if type(this_level_values[left]) != int:
#                     left += 1
#                 else:
#                     right -=1
#             width = (right+1) - left
#             max_width = max(width, max_width)
#             #print(max_width)
            
#             this_level = next_level
        
#         return max_width