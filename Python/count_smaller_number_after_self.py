from typing import List
class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    if nums == None:
      return []
    count = [0] * len(nums)
    # make pair of nums value and their indices:
    numsWithIndices = [] #List[List[int]]
    for i in range(len(nums)):
      numsWithIndices.append([nums[i], i])
    
    def merge(count: List[int], beg: int, mid: int, end: int):
      i, j = beg, mid
      temp = []
      while i != mid and j != end:
        if numsWithIndices[i][0] < numsWithIndices[j][0]:
          temp.append(numsWithIndices[i])
          count[numsWithIndices[i][1]]+=j-mid
          i+=1
        else:
          temp.append(numsWithIndices[j])
          j+=1
      while i != mid:
        temp.append(numsWithIndices[i])
        count[numsWithIndices[i][1]]+=j-mid
        i+=1
      while j != end:
        temp.append(numsWithIndices[j])
        j+=1
      for i in range(len(temp)):
        numsWithIndices[i+beg] = temp[i]
          
    def mergeSort(count: List[int], numsWithIndices: List[List[int]], beg: int, end: int):
      if end - beg <= 1:
        return
      mid = int((beg+end)/2)
      mergeSort(count, numsWithIndices, beg, mid)
      mergeSort(count, numsWithIndices, mid, end)
      merge(count, beg, mid, end)
      print(numsWithIndices)
    
    mergeSort(count, numsWithIndices, 0, len(nums))    
    return count
  
nums = [5,2,6,1]
print(Solution().countSmaller(nums))