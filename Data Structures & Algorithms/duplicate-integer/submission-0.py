class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique = set(nums)

        for num in unique:
            if len(unique) < len(nums):
                return True

        return False