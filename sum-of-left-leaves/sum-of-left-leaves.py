# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        '''
        sum += value of current left + val going left
        sum += go right
        
        return sum
        '''
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return 0
        
        sum_left_leaves = self.getSum(root)
        
        return sum_left_leaves
        
    def getSum(self, root):
        
        if root.left is None and root.right is None:
            return root.val
        
        left = 0
        if root.left:
            left = self.getSum(root.left)
        
        right = 0
        if root.right:
            if root.right.left is None and root.right.right is None:
                right = 0
            else:
                right = self.getSum(root.right)
                
        
        return left + right
        