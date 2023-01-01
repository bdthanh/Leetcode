class Solution1:
  def fib(self, n: int) -> int:
    fibo = [0]*(n+1)
    fibo[0] = 0
    if n == 0:
      return fibo[0]
    fibo[1] = 1 
    if n == 1:
      return fibo[1]
    i = 1
    while i != n:
      i+=1
      fibo[i] = fibo[i-1]+fibo[i-2]
    return fibo[n]
    
class Solution2:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]