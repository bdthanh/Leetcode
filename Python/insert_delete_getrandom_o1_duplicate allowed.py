from random import randint
from collections import defaultdict
from typing import Set
class RandomizedCollection:
  def __init__(self):
    self.store = []
    self.mapPos = defaultdict(set)

  def insert(self, val: int) -> bool:
    self.store.append(val)
    self.mapPos[val].add(len(self.store)-1)
    return len(mapPos[val]) == 1

  def remove(self, val: int) -> bool:
    if self.mapPos[val]:
      pos = self.mapPos[val].pop()
      self.mapPos[self.store[-1]].add(pos)
      self.mapPos[self.store[-1]].remove(len(self.store)-1)
      self.store[-1], self.store[pos] = self.store[pos], self.store[-1]
      self.store.pop()
      return True
    return False
       

  def getRandom(self) -> int:
    return self.store[randint(0, len(self.store)-1)]