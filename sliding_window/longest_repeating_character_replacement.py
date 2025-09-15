"""
1. initialize a hm and initialize l, output, windowsize = 0
2. for loop for right pointer
3. at new index, check whether k is satisfied, while it isnt, shift l by 1
    while windowSize - maxOccurence > k:
        hm[s[l]] -= 1
        l+=1
    windowsize: r-l+1
    k = windowsize - maxOccurence
    maxOccurence = max(hm.values())
4. add current index to hm
5. calculate max length of window 
    output = max(output, r-l+1)
6. return output

A:4
B:2
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l = 0
        output = 0
        window_size = 0

        for r in range(len(s)):
            window_size = r-l+1
            char_freq[s[r]] += 1
            while window_size - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l+=1
                window_size = r-l+1
            output = max(output, window_size)
        
        return output






