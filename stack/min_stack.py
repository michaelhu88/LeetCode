"""
we cant use 1 list because getMin() won't be constant time.
we cant use 1 list and 1 running variable, because we won't know what the next smallest value is in case of a pop


pop removes, but doesnt return
top doesnt remove, but returns
arr = [-2]
min_list = [-2]
arr.pop()
arr[-1]
var = -3

constructor:
    -two lists
        -normal stack
        -current minimum list
push:
    -trivial for normal stack
    -min list: if empty, then trivial
        -else, compare val with minlist[-1]
pop:
    -trivial
top:
    -trivial

getMin:
    -trivial
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_list:
            self.min_list.append(val)
        else:
            self.min_list.append(min(val, self.min_list[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_list.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]