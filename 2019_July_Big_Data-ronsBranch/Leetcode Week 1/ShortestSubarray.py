import collections

class Solution:
    def shortestSubarray(self, A, K):
        """A: List[int] , K: int"""
        N = len(A)
        pre_sum = [0] * (N + 1)
        for i, n in enumerate(A):
            pre_sum[i + 1] = pre_sum[i] + n

        ans = N + 1
        queue = collections.deque()

        for j in range(N + 1):
            while queue and pre_sum[queue[-1]] >= pre_sum[j]:
                queue.pop()

            while queue and pre_sum[j] - pre_sum[queue[0]] >= K:
                i = queue.popleft()
                ans = min(ans, j - i)

            queue.append(j)

        return ans if ans < N + 1 else -1
