class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0,0]
        for m in moves:
            if m == 'U':
                pos[0] += 1
            elif m == 'D':
                pos[0] -= 1
            elif m == 'L':
                pos[1] -= 1
            elif m == 'R':
                pos[1] += 1
        return pos == [0,0]