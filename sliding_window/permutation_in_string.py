class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        first_length = len(s1)
        first_counts = [0] * 26
        second_counts = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            first_counts[index] += 1
        
        for i in range(first_length):
            index = ord(s2[i])-ord('a')
            second_counts[index] += 1
        
        l = 0
        r = first_length
        while r < len(s2):
            if second_counts == first_counts:
                return True
            second_counts[ord(s2[l])-ord('a')] -= 1
            second_counts[ord(s2[r])-ord('a')] += 1
            l+=1
            r+=1
        if second_counts == first_counts:
            return True
        return False

