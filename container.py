class Solution(object):
    def maxArea(self, nums):
        left=0
        right =len(nums)-1
        max_water = 0

        while left < right:
            area=min(nums[left], nums[right]) * (right - left)

            max_water = max(max_water, area)

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return max_water
 
