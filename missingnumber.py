class Solution(object):
    def missingNumber(self, nums):
       l=list(set(list(range(len(nums)+1)))-set(nums))
       return l[0]
