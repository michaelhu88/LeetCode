class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                value = num
                cur_sequence = 0
                while value in numSet:
                    cur_sequence += 1
                    value += 1
                longest = max(longest, cur_sequence)
        
        return longest
