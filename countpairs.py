class Solution(object):
    def countPairs(self, nums, target):
        saver=[]
        for i in range(len(nums)):
            
            for j in range(i,len(nums)):
                if nums[i]+nums[j]< target and i!=j:
                    saver.append((i,j))
        return len(saver)
