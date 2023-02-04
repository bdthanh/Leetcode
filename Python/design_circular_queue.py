class MyCircularQueue:

  def __init__(self, k: int):
    self.len = k
    self.rear = k-1
    self.front = 0
    self.queue = [None for _ in range(k)]
        

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False
    if self.rear + 1 == self.len:
      self.rear = 0
    else:
      self.rear += 1
    self.queue[self.rear] = value
    return True
        

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    self.queue[self.front] = None
    if self.front + 1 == self.len:
      self.front = 0
    else:
      self.front += 1
    return True
          

  def Front(self) -> int:
    return self.queue[self.front] if not self.isEmpty() else -1

  def Rear(self) -> int:
    return self.queue[self.rear] if not self.isEmpty() else -1  

  def isEmpty(self) -> bool:
    return (self.rear == self.front-1 or (self.rear == self.len-1 and self.front == 0)) and self.queue[self.rear] == None
        

  def isFull(self) -> bool:
    return (self.rear == self.front-1 or (self.rear == self.len-1 and self.front == 0)) and self.queue[self.rear] != None
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
print(obj.queue)
param_2 = obj.enQueue(2)
print(obj.queue)
param_3 = obj.enQueue(3)
print(obj.queue)
param_35 = obj.enQueue(4)
print(obj.queue)
param_4 = obj.deQueue()
print(obj.queue)
param_5 = obj.Front()
print(obj.queue)
param_6 = obj.Rear()
print(obj.queue)
param_7 = obj.isEmpty()
print(obj.queue)
param_8 = obj.isFull()
print(obj.queue)
print(param_1,param_2,param_3,param_4,param_5,param_6)