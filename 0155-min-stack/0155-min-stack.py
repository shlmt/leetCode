class MinStack(object):

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        if len(self.m)>0:
            self.m.append(min(val,self.m[-1]))
        else:
            self.m.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.m.pop(-1)
        self.s.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.insert(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()