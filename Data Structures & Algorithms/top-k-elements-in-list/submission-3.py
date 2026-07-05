class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums: 
            if n not in count: 
                count[n] = 0

            count[n] += 1

        buckets = [[] for _ in range(len(nums)+1)]

        for n, freq in count.items(): 
            buckets[freq].append(n)

        result = []

        for freq in range(len(buckets) - 1, 0, -1): 
            for n in buckets[freq]: 
                result.append(n)

                if len(result) == k: 
                    return result