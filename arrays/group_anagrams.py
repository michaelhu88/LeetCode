"""

list = []
tuple(list)

1. initialize a dictionary
2. iterate through the input array
    -create array [0] * 26
    -iterate through the chars
        -ord(char)-ord('a'), increment the array
    -convert array to tuple
    -dict[tuple].append(word)

{(tup): [word1,word2], }

Space = O(n) where n is the number of words in strs
Time = O(m*n) where m is the number of words and n is the average length of word
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            arr = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                arr[index]+=1
            anagrams[tuple(arr)].append(word)
        
        return list(anagrams.values())
        