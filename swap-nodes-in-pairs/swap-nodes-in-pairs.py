# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swapper(head)
    
    '''
    A. Recursive approach
    '''
    
#     def swapper(self, head):
#         # Base case: if the input is not empty or has more than one node left
#         if head and head.next:
            
#             # nodes to be swapped
#             firstNode = head
#             secondNode = head.next
            
#             # swap nodes
#             firstNode.next = self.swapper(secondNode.next)
#             secondNode.next = firstNode
            
#             return secondNode
            
#         return head

    '''
    B. Iterative approach
    '''
    
    def swapper(self, head):
        
        dummy = ListNode(-1)
        dummy.next = head
        
        prevNode = dummy
        
        while head and head.next:
            
            firstNode = head
            secondNode = head.next
            
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            prevNode.next = secondNode
            
            head = firstNode.next
            prevNode = firstNode
       
        return dummy.next
            
        