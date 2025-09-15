"""
1. min_element variable
2. normal binary search setup
3. always compare is l > r
    if so, we know there are two ascending lines
    so to find min we go to the right

    else, we search on the left
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_element = math.inf
        l = 0 
        r = len(nums)-1

        while l <= r:
            m = (l+r) // 2
            min_element = min(min_element, nums[m])

            if nums[l] > nums[r]:
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r = m - 1
        
        return min_element
        