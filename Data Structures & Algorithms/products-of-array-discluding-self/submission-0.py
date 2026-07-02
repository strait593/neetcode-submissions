class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        forward_prod = 1
        for i in range(n):
            output[i] = forward_prod
            forward_prod *= nums[i]
        
        backwards_prod = 1
        for i in range(n -1, -1, -1):
            output[i] *= backwards_prod
            backwards_prod *= nums[i]

        return output