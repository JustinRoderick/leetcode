# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_head = ListNode()
        temp = answer_head
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            num = l1_val + l2_val + carry

            temp.next = ListNode()
            temp = temp.next
            temp.val = num
           
            if temp.val >= 10:
                temp.val = num % 10
                carry = num // 10

            if temp.val < 10:
                carry = num // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            temp.next = ListNode(carry)
        
        return answer_head.next