# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# steps
# base case: if l1 and l2 is null
# recursive case: 
# sum = l1.val + l2.val + carry
# carry = sum - 10 if sum > 10
# new val
# return listNode(new val, recurse(l1, l2, carry))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            if l2 is None:
                return None
            return l2
        elif l2 is None:
            return l2
        else:
            return self.helper(l1, l2)
    
    def helper(self, l1, l2):
        sum_ = l1.val + l2.val
        digit, tenth = sum_%10, sum_//10
        if l1.next or l2.next or tenth:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val = l1.val + tenth
            return ListNode(digit, self.helper(l1, l2))
        return ListNode(digit)
        