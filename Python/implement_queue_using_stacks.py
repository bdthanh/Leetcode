class MyQueue:
  def __init__(self):
     self.ori = []
     self.temp = []
     self.top = -1   

  def push(self, x: int) -> None:
    self.ori.append(x)
    if len(self.ori) == 1:
      self.top == x
    

  def pop(self) -> int:
    top = self.top
    while len(self.ori) != 1:
      self.temp.append(self.ori[-1])
      self.ori.pop()
    self.top = self.temp[-1] if len(self.temp) != 0 else -1
    self.ori.pop()
    while len(self.temp) != 0:
      self.ori.append(self.temp[-1])
      self.temp.pop()
    return top

  def peek(self) -> int:
    return self.top

  def empty(self) -> bool:
    return True if len(self.ori) == 0 else False 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()