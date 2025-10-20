# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        temp = head
        while temp:
            if temp.next:
                count += 1
            temp = temp.next
        
        if count == 1:
            return None
        if count == n:
            return head.next
        
        temp = head
        for _ in range(count - (n+1)):
            temp = temp.next
        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        
        return head