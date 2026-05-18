class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in targets:
                return [targets[compliment], i]
            
            targets[nums[i]] = i
        
        return []