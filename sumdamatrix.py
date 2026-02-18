class Solution(object):
    def matrixSum(self, nums):
                score = 0
                while any(nums):  #somehow any workd okay 
                    bigboss = []
                    for row in nums:
                            if row:
                                m = max(row)
                                row.remove(m)
                                bigboss.append(m)
                    score += max(bigboss)
                return score
