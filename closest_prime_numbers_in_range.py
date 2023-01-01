from typing import List
from math import sqrt
class Solution:
  def closestPrimes(self, left: int, right: int) -> List[int]:
    def isPrime(num: int) -> bool:
      if num < 1: 
        return False
      if num == 2:
        return True
      for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
          return False
      return True
    primes = []
    minDist = 2147483647
    for i in range(left, right+1):
      if isPrime(i):
        primes.append(i)
        
    if len(primes) <= 1:
      return [-1,-1]
    minid = -1
    for i in range(len(primes)-1):
      if minDist > primes[i+1]-primes[i]:
        minDist = primes[i+1]-primes[i]
        minid = i
    return [primes[minid], primes[minid+1]]

left = 19
right = 31
print(Solution().closestPrimes(left, right))
        
        
          