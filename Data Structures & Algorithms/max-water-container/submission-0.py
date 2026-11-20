class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            cur_area = min(heights[left], heights[right]) * (right - left)

            if heights[left] > heights[right]:
                right -=1
            elif heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            
            max_area = max(max_area, cur_area)

        return max_area

        