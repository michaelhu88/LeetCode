"""
1. initialize left = 0, initialize a set, and a output variable
2. iterate through each index with right
3. if right not in set, add to set
4. else, while left != right, delete left from set and move left + 1
5. output = r - l + 1

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        my_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l+=1
            
            
        return output