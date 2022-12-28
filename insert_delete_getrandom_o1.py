from random import randint
class RandomizedSet:
  def __init__(self):
    self.store = []
    self.mapPos = {}

  def insert(self, val: int) -> bool:
    if self.mapPos.get(val) == None:
      self.store.append(val)
      self.mapPos[val] = len(self.store)-1   
      return True
    return False

  def remove(self, val: int) -> bool:
    if self.mapPos.get(val) != None:
      pos = self.mapPos[val]
      self.mapPos[self.store[-1]] = pos
      self.store[-1], self.store[pos] = self.store[pos], self.store[-1]
      self.store.pop()
      self.mapPos.pop(val)
      return True
    return False
       

  def getRandom(self) -> int:
    return self.store[randint(0, len(self.store)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_1,param_2, param_3)