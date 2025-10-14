# 150. Evaluate Reverse Polish Notation

import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
        operation = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),
        }

        for i in range(n - 1):
            if tokens[i] not in operation:
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operation[tokens[i]](num2, num1))
        
        num1 = stack.pop()
        num2 = stack.pop()
        return operation[tokens[n-1]](num2, num1)