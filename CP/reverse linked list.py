class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def iterative(head):
            pre,cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def recursively(head):
            if not head or not head.next:
                return head
            node = recursively(head.next)
            head.next.next = head
            head.next = None
            return node
        
        return iterative(head)
