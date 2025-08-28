# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        #base case 
        if not root: 
            return False 
    
        # check if it's leaf node 
        if not root.left and not root.right : 
            return targetSum == root.val
        remaining = targetSum-root.val

        return (self.hasPathSum(root.left, remaining)) or (self.hasPathSum(root.right, remaining))



        