from heapq import heappush, heappop


def __init__(self):
    self.max_heap = []  # for half left
    self.min_heap = []  # for half right


def addNum(self, num):
    size_left = len(self.max_heap)
    size_right = len(self.min_heap)
    if size_left == 0 and size_right == 0:
        heappush(self.min_heap, num)
        return

    if self.max_heap:
        left_val = -self.max_heap[0]
    if self.min_heap:
        right_val = self.min_heap[0]

    if size_left == size_right:
        if num <= left_val:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
    elif size_left > size_right:
        if num >= left_val:
            heappush(self.min_heap, num)  # then balance
        else:
            tmp = heappop(self.max_heap)
            heappush(self.min_heap, -tmp)
            heappush(self.max_heap, -num)
    else:  # size_left < size_right
        if num < right_val:
            heappush(self.max_heap, -num)  # then balance
        else:
            tmp = heappop(self.min_heap)
            heappush(self.max_heap, -tmp)
            heappush(self.min_heap, num)


def findMedian(self):
    size_left = len(self.max_heap)
    size_right = len(self.min_heap)

    if size_left == size_right:
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
    elif size_left > size_right:
        return float(-self.max_heap[0])
    else:
        return float(self.min_heap[0])