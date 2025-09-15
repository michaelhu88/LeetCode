class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                value, index = stack.pop()
                output[index] = (i - index)
            stack.append((temperatures[i], i))
        
        return output
