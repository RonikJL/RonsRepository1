class MovingAverage(object):
    def __init__(self, size):
        from collections import deque

        self.size = size
        self.windowLen = 0
        self.windowSum = 0
        self.windowQue = deque()

    def next(self, val):

        self.windowLen += 1
        self.windowQue.append(val)
        self.windowSum += val

        if self.windowLen > self.size:
            self.windowLen -= 1
            self.windowSum -= self.windowQue.popleft()

        return float(self.windowSum) / float(self.windowLen)


