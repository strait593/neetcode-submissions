class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]

        if not nums:
            return 0

        nums = sorted(list(set(nums)))

        count_current = 1
        count_longest = 1

        for i in range(len(nums) - 1):
            current_item = nums[i]
            next_item = nums[i + 1]

            if next_item == current_item + 1:
                count_current += 1
            else:
                count_longest = max(count_longest, count_current)
                count_current = 1

        return max(count_longest, count_current)