class Solution(object):
    def findMaxAverage(self, nums, k):
                cursum = sum(nums[:k])
                max_sum = cursum
                for i in range(k, len(nums)):
                    cursum = cursum - nums[i - k] + nums[i]
                    max_sum = max(max_sum, curr_sum)
                return max_sum / float(k)  
