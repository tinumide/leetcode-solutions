# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        1 -> 2 -> 3 -> 4 -> 5
        2 -> 1 -> 4 -> 3 -> 5
        
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        2 -> 1 -> 4 -> 3 -> 6 -> 5
        '''
        if head is None or head.next is None:
            return head
        curr = head
        nxt = head.next
        
        curr.next = self.swapPairs(nxt.next)
        nxt.next = curr
        return nxt

        
        
        
        
        
        
        
        
        #         if head is None or head.next is None:
#             return head
#         curr = head
#         nxt = head.next
#         curr.next = nxt.next
#         nxt.next = curr
#         head = nxt
#         if head.next.next:
#             self.swapper(head.next, head.next.next, head.next.next.next)
#         return head
    
#     def swapper(self, prev, curr, nxt):
#         if curr is None or nxt is None:
#             return
#         curr.next = nxt.next
#         nxt.next = curr
#         prev.next = nxt
#         if nxt.next.next:
#             self.swapper(nxt.next, nxt.next.next, nxt.next.next.next)
#         return
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
#     def swapper(self, head):
        
#         dummy = ListNode(-1)
#         dummy.next = head
        
#         prevNode = dummy
        
#         while head and head.next:
            
#             firstNode = head
#             secondNode = head.next
            
#             firstNode.next = secondNode.next
#             secondNode.next = firstNode
            
#             prevNode.next = secondNode
            
#             head = firstNode.next
#             prevNode = firstNode
       
#         return dummy.next
            
        