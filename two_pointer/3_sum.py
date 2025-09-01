"""
-4,-1,-1,0,1,2

0. initialize output array, sort, keep track of previous var
1. outer for-loop where we isolate index (target), set prev = current index
    -we are only examining indexes to the right
        -apply two pointer to this portion of array
            -if sum == (-target), then append output (check all possible)
2. as we increment outer for-loop, while next value = prev, skip
return output
"""
import math
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        prev = -math.inf
        for i in range(len(nums)):
            if prev == nums[i]:
                continue
            if nums[i] > 0:
                return output
            if i == len(nums) - 1:
                return output
            target = -(nums[i])
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            prev = nums[i]

        return output
            

            








        