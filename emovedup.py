class Solution(object):
    def removeDuplicates(self, nums):
        islow = 0  # tow pointers this is slow 
        for jj in range(1, len(nums)):
            if nums[jj] !=nums[islow]:
                islow += 1
                nums[islow] =nums[jj]
        return islow+1
