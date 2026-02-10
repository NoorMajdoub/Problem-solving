from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):
        n=len(nums)
        l=Counter(nums)
        return [x for x in l if l[x]==2]
