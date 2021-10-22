# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
       -1 -> 6 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None
       -1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None
       -1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                  
       -1 -> 2 -> 3 -> 4 -> 5 -> None
        '''
        prev = ListNode(-1, head)
        
        self.helper(prev, head, val)
        
        return prev.next
    
    def helper(self, prev, curr, val):
        
        if curr is None:
            return
        
        if curr.val == val:
            prev.next = curr.next
            self.helper(prev, curr.next, val)
        else:
            self.helper(curr, curr.next, val)
        
        return
        