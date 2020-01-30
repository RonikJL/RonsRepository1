import collections
from _ast import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt, res = collections.Counter(), 0
        for t in time:
            res += cnt[60 - t % 60] if t % 60 else cnt[0]
            cnt[t % 60] += 1
        return res