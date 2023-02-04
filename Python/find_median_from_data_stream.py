from queue import PriorityQueue
class MedianFinder:
  def __init__(self):
    self.queueHigh = PriorityQueue() 
    self.queueLow  = PriorityQueue() 
    self.median = 0
        
  def addNum(self, num: int) -> None:
    if self.queueHigh.qsize() == self.queueLow.qsize() == 0:
      self.median = num
      self.queueHigh.put(num)
    elif self.queueLow.qsize() == self.queueHigh.qsize():
      if num <= -self.queueLow.queue[0]:
        self.queueHigh.put(-self.queueLow.get())
        self.queueLow.put(-num)
      else: # num >= -self.queueHigh.queue[0]
        self.queueHigh.put(num)
      self.median = self.queueHigh.queue[0]
    elif self.queueLow.qsize() < self.queueHigh.qsize():
      if num < self.queueHigh.queue[0]:
        self.queueLow.put(-num)
      else: # num >= -self.queueHigh.queue[0]
        self.queueLow.put(-self.queueHigh.get())
        self.queueHigh.put(num)
      self.median = (- self.queueLow.queue[0] + self.queueHigh.queue[0])/2    
    print(self.queueLow.queue)
    print(self.queueHigh.queue)   
  def findMedian(self) -> float:
    return self.median
        
mf = MedianFinder()
mf.addNum(6)
print(mf.findMedian())
mf.addNum(10)
print(mf.findMedian())
mf.addNum(2)
print(mf.findMedian())
mf.addNum(14)
print(mf.findMedian())
mf.addNum(35)
print(mf.findMedian())
mf.addNum(19)
print(mf.findMedian())
mf.addNum(34)
print(mf.findMedian())
mf.addNum(35)
print(mf.findMedian())
mf.addNum(28)
print(mf.findMedian())
mf.addNum(35)
print(mf.findMedian())
mf.addNum(26)
print(mf.findMedian())
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()