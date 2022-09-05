"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# all_levels = [[1],[3,2,4],[5,6] ]
# this_level = [5,6] 
# this_level_values = [5,6] 
# next_level_nodes = [] 
# this_level = next_level_nodes

#                         1
#                 /.     |.     \
#               3        2.     4
#             /. \
#         5      6
            
            

    
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []

        all_levels = []
        this_level = [root]

        while this_level:
            this_level_values = []
            next_level_nodes = []
            for node in this_level:
                this_level_values.append(node.val)
                if node.children:
                    next_level_nodes += node.children
            all_levels.append(this_level_values)

            # next_level_nodes = []
            # for node in this_level:
            #     if node.children:
            #         next_level_nodes += node.children
            this_level = next_level_nodes  
        return all_levels
        