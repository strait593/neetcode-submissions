class Solution:
    def trap(self, height: List[int]) -> int:
        maximum_left = []
        maximum_right = []
        trapped_water = 0

        left_max = 0
        for h in height:
            left_max = max(left_max, h)
            maximum_left.append(left_max)

        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            right_max = max(right_max, height[i])
            maximum_right.insert(0, right_max)

        for i in range(len(height)):
            water = min(maximum_left[i], maximum_right[i]) - height[i]
            if water > 0:
                trapped_water += water

        return trapped_water