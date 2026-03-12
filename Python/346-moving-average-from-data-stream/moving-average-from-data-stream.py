class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size=size
        self.queue=[]

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """ 
        self.queue.append(val)
        total=sum(self.queue[-self.size:])

        return total*1.0/min(len(self.queue),self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)