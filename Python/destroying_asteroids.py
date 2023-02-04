class Solution:
  def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
    asteroids = sorted(asteroids)
    for asteroid in asteroids:
      if mass >= asteroid:
        mass+=asteroid
      else:
        return False
    return True