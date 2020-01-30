from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        a = []
        ans = None
        p = ans
        for i in range(len(lists)):
            if lists[i]:
                a.append((lists[i].val,i))
        heapify(a)
        while a:
            (val,idx) = heappop(a)
            if not p:
                p = ListNode(val)
                ans = p
            else:
                p.next = ListNode(val)
                p = p.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(a,(lists[idx].val,idx))
        return ans