class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        left_to_right_prod = 1
        right_to_left_prod = 1

        for i in range(len(nums)):
            result[i] = left_to_right_prod
            left_to_right_prod *= nums[i]
        for i in range(len((nums)) - 1, -1, -1):
            result[i] *= right_to_left_prod
            right_to_left_prod *= nums[i]

        return result 
        