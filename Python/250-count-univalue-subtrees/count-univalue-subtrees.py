# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0 

        def isunival(root):

            if not root: 
                return True 

            left_ok=isunival(root.left)
            right_ok=isunival(root.right)

            if left_ok and right_ok: 
                if root.left and root.val!=root.left.val:
                    return False
                if root.right and root.val!=root.right.val:
                    return False

                self.count+=1
                return True

        isunival(root)
        return self.count
                

            
        
            
        