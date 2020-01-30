from _ast import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for number in A:
            result.append(number*number)
        return sorted(result)
