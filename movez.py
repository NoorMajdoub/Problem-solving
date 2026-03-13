class Solution(object):
    def moveZeroes(self, nums):
        last0 =0 

        for current in range(len(nums)):
            if nums[current]!= 0:
#on first elem that both is 0 non happen until we find the first non 0
                nums[last0], nums[current] = nums[current], nums[last0]
                last0 += 1
