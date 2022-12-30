import heapq
from operator import itemgetter
from typing import List
class Solution:
  def getOrder(self, tasks: List[List[int]]) -> List[int]:
    for i in range(len(tasks)):
      tasks[i].append(i)
    tasks = sorted(tasks, key=itemgetter(0))
    ans = []
    waitingQueue = []

    # only use this outer loop for idle case
    while len(tasks) != 0:
      time = tasks[0][0]
      
      #get all waiting tasks and sort them by our custom comparator
      while len(tasks) != 0 and time >= tasks[0][0]:
        waitingTask = tasks.pop(0)
        heapq.heappush(waitingQueue, waitingTask[1:3])
      # running until there is no waiting task (idle)
      while len(waitingQueue) != 0:
        curTask = heapq.heappop(waitingQueue)
        time += curTask[0]
        ans.append(curTask[1])
        while len(tasks) != 0 and time >= tasks[0][0]:
          waitingTask = tasks.pop(0)
          heapq.heappush(waitingQueue, waitingTask[1:3])
          
    return ans
  
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
print(Solution().getOrder(tasks))
    