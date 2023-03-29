# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        def inOrder(node, visited, result):
            if node is None:
                return result, visited
            
            #visit left node
            result,visited =inOrder(node.left, visited, result)
            # print(node.val, result, visited)
            
            #visit current, update visited count, check if visited is our K value, If so, save that into result
            visited += 1
            if visited == k:
                # print(f'our k value should be {node.val}')
                result = node.val
                
            
            #visit right node
            result,visited = inOrder(node.right, visited, result)
            
            return result,visited 
            
        result,visited = inOrder(root, 0, -1)
        print(result)
        return result
            
              