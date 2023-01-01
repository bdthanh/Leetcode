from typing import List
class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
      # all the case a asteroid can be added without pop any existed one
      if len(stack) == 0 or asteroid > 0 or (asteroid < 0 and stack[-1] * asteroid > 0):
        stack.append(asteroid)
      # cases when asteroid < 0
      elif asteroid < 0:
        # loop to remove some bacause of collision
        while len(stack) != 0 and abs(asteroid) > stack[-1] > 0:
          stack.pop(-1)
        # handle cases causing the loop end
        if len(stack) == 0 or asteroid * stack[-1] > 0:
          stack.append(asteroid)
        elif abs(asteroid) == stack[-1]:
          stack.pop(-1)
    return stack
      