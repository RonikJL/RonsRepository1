class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and slow:
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break

        return False


