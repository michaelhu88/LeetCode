"""
make sure to int() for division
when popping, one, two; two operand one
1) initialize stack
2) iterate thru tokens
    -if integer, add to stack
    -if operand, pop 2 items in stack and calculate, 
    and add back result to stack
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        token_list = ["+", "-", "*", "/"]

        for token in tokens:
            if token in token_list:
                one, two = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(two + one)
                elif token == "-":
                    stack.append(two - one)
                elif token == "*":
                    stack.append(two * one)
                else:
                    stack.append(int(two/one))
            else:
                stack.append(int(token))
        
        return stack[0]