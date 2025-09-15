class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        occurence = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1

        for num, v in counts.items():
            occurence[v].append(num)
        
        res = []
        for i in range(len(occurence) - 1, 0, -1):
            for num in occurence[i]:
                res.append(num)
                if len(res) == k:
                    return res
