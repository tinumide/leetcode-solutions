# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        power,val = self.converter(curr)
        return val
    
    def converter(self, curr):
        '''
        if curr is not None:
            power, val = self.converter(curr.next)
            return (power*2, curr.val*power + val)
        else:
            return(1, 0)
        '''
        if curr is None:
            return (1, 0)
        power, val = self.converter(curr.next)
        return (power * 2, curr.val * power + val)