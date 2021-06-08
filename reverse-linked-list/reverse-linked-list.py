# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        head = self.helper(prev, head)
        return head
        
    
#     '''
#     A. Recursive approach
#     '''
    
#     def helper(self, prev, head ):
#         # Base case: if there's no node left in the list
#         if head is None:
#             head = prev
#             return head
        
#         # reverse next pointer of current node
        
#         newHead = head.next
#         head.next = prev
        
#         return self.helper(head, newHead)
    
    '''
    B. Iterative approach
    '''
    
    def helper(self, prev, head):
        while head is not None:
            
            # reverse
            newHead = head.next
            head.next = prev
            
            # reassign
            prev = head
            head = newHead
        
        return prev
            
            
        