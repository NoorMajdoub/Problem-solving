class Solution(object):
    def pivotIndex(self, nums):
        s=sum(nums)
        current=0
        for i in range(len(nums)):
            if current==s-current-nums[i]:
               return i
        # if current==s-current:
        #     print(i)
        #     break
            current+=nums[i]
        if i ==len(nums)-1:
            return -1
