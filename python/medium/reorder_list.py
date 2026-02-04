# 143. Reorder List

# Determine the middle of the list, reverse the second half of the list, and merge the two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev   

    def merge_list(self, first: Optional[ListNode], second: Optional[ListNode]) -> ListNode:
        while second:
            temp_first = first.next
            temp_second = second.next

            first.next = second
            second.next = temp_first

            first = temp_first
            second = temp_second

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        n = 1
        while cur.next != None:
            n += 1
            cur = cur.next
        if n < 3:
            return head
        cur = head
        if n % 2 != 0:
            n += 1
        mid = n // 2
        
        n = 1
        while n < mid:
            n += 1
            cur = cur.next

        second = cur.next
        cur.next = None
        self.merge_list(head, self.reverse_list(second))
        