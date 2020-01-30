class MinStack(object):
    stack = []
    order_stack = []  # save the index

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.order_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.order_stack) == 0 or self.stack[self.order_stack[-1]] > x:
            self.order_stack.append(len(self.stack) - 1)

    def pop(self):
        """
        :rtype: None
        """
        res = self.stack.pop()
        if len(self.stack) == self.order_stack[-1]:
            self.order_stack.pop()
        return res

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.order_stack[-1]]
