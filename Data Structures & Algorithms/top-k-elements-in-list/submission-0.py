class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] +=1

        unique_numbers = list(counter.keys())

        unique_numbers.sort(key=lambda x: counter[x], reverse=True)
        
        return unique_numbers[:k]