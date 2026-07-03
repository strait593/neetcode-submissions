class Solution:
    def median(self, numbers):
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
    
        mid = n // 2

        if n % 2 != 0:
            return sorted_nums[mid]
        else:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
         
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        big_array = nums1 + nums2

        return self.median(big_array)