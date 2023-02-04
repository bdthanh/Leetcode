from typing import List
class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    toVisitRooms = []
    for key in rooms[0]:
      toVisitRooms.append(key)
    visited.add(0)
    while len(toVisitRooms) != 0:
      curRoom = toVisitRooms.pop()
      for key in rooms[curRoom]:
        if not key in visited:
          toVisitRooms.append(key)
      visited.add(curRoom)
    if len(visited) == len(rooms):
      return True
    return False
  
rooms = [[1],[2],[3],[]]
print(Solution().canVisitAllRooms(rooms))
        