class Solution(object):
    def sortColors(self, nums):
            n = len(nums)
            for i in range(n-1):
                min_index = i
                for j in range(i+1, n):
                    if nums[j] < nums[min_index]:
                        min_index = j
                min_value = nums.pop(min_index)
                nums.insert(i, min_value)
