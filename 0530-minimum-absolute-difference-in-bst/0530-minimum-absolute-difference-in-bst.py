# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        nums = []
        
        def inOrder(node):
            nonlocal nums
            
            if not node:
                return
            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)
            
            
        inOrder(root)
        print(nums)
        
        min_diff = float('inf')
        for i in range(1,len(nums)):
            min_diff = min(min_diff,nums[i]-nums[i-1])
        return min_diff
        