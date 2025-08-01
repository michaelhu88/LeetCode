class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_array = [0] * 26
        t_array = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            s_array[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            t_array[index] += 1
        
        return s_array == t_array