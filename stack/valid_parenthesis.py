class Solution:
    def isValid(self, s: str) -> bool:

        hm = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in hm:
                if stack:
                    last_open = stack.pop()
                    if last_open != hm[char]:
                        return False       
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        return False