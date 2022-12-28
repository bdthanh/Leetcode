from typing import List 

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    def getNums(stack) -> int:
      num2 = stack.pop()
      num1 = stack.pop()
      return num1, num2
    result = None
    stack = []
    for i in range(len(tokens)):
      if tokens[i] == "+":
        num1, num2 = getNums(stack)
        stack.append(num1+num2)
      elif tokens[i] == "-":
        num1, num2 = getNums(stack)
        stack.append(num1-num2)
      elif tokens[i] == "*":
        num1, num2 = getNums(stack)
        stack.append(num1*num2)
      elif tokens[i] == "/":
        num1, num2 = getNums(stack)
        stack.append(int(num1/num2))
      else:
        stack.append(int(tokens[i]))
    return stack[0]

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))
        