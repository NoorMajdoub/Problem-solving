class Solution(object):
    def thirdMax(self, nums):
        if len(set (nums) )<3:
            return max(nums)
        return sorted(list(set(nums)),reverse=True)[2]

