from sortedcontainers import SortedDict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = SortedDict()
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
        res = list(numMap.keys())
        res.sort(key = lambda x : numMap[x])
        return res[-k:]
        