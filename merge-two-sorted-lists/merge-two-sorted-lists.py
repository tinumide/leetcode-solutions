# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# l1 = 1  2 7
# l2 = 0  5 6 8
#
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        1 - 2 - 4 - 5 - None
        1 - 3 - 4 - None
        
        5 - None
        1 - 2 - 4 - None
        
        1 - 5 - None
            2 - 4 - None
        '''
        if l1 is None:
            return l2
        
        elif l2 is None:
            return l1
        
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        