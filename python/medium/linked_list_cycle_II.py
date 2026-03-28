# 142. Linked List Cycle II

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.cycleLength(slow, head)
        return None
        
    def cycleLength(self, slow: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        while head and slow:
            if head == slow:
                return head
            head = head.next
            slow = slow.next

# little bit faster

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head and slow:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None

