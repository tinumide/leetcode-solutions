import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
                            3
                            
                t    1                   5 
                    
                                    4        6
                                    
                                2                 7
                            
        '''
        isValid = self.validator(root)
        
        return isValid
    
    
    def validator(self, root, lowerbound=-math.inf, upperbound=math.inf):
        
        if root is None:
            return True
        
        if root.val <= lowerbound or root.val >= upperbound:
            return False
        
        left = self.validator(root.left, lowerbound, root.val)
        
        right = self.validator(root.right, root.val, upperbound)
        
        return left and right
        
        
        