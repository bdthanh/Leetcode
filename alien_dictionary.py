from collections import defaultdict
from typing import List, Dict
class Solution:
  def alienOrder(self, words: List[str]) -> str:
    def getGraph(words: List[str]):
      i = 0
      dic = defaultdict(list)
      while i != len(words)-1: # the last word has nothing to compare with so we stop at len(words)-2
        smaller_len = min(len(words[i]), len(words[i+1]))
        j=0
        isSubstring = True
        while j < smaller_len:
          if words[i][j] != words[i+1][j]:
            isSubstring = False
            dic[words[i+1][j]].append(words[i][j])
            break
          j+=1
        if isSubstring and len(words[i+1]) < len(words[i]):
          return -1
        i+=1
      return dic
    
    def toposort(dic: Dict[str, List[str]], sortedStr: str, visited) -> str:
      for key in visited.keys():
        if visited.get(key) == False:
          sortedStr = toposortUtil(dic, sortedStr, visited, key)
      return sortedStr
          
    def toposortUtil(dic: Dict[str, List[str]], sortedStr: str, visited, key: str) -> str:
      visited[key] = True
      for item in dic[key]:
        if visited[item] == False:
          sortedStr = toposortUtil(dic, sortedStr, visited, item)
      sortedStr+=(key)
      return sortedStr
    
    def isCyclic(dic: Dict[str, List[str]], pos: Dict[str, int]):
      for key in dic.keys():
        for item in dic.get(key):
          if (pos.get(item) > pos.get(key)):
            return True
      return False
      
    dic = getGraph(words) 
    if dic == -1:
      return ""   
    sortedStr = ""
    visited = {}
    for i in range(len(words)):
      for j in range(len(words[i])):
        visited[words[i][j]] = False
    sortedStr = toposort(dic, sortedStr, visited) 
    
    #check if the dictionary/graph is cyclic or not
    pos = {}
    for i in range(len(sortedStr)):
      pos[sortedStr[i]] = i
    if isCyclic(dic, pos):
      sortedStr = ""
    return sortedStr
      
words = ["z", "z"]
print(Solution().alienOrder(words))    
    
    