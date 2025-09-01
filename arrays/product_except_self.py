class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        running = 1
        for num in nums:
            running *= num
            prefix.append(running)
        running = 1
        for i in range(len(nums)-1, -1, -1):
            running *= nums[i]
            postfix[i] = running
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[1])
            elif i == (len(nums)-1):
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1]*postfix[i+1])
        return output



