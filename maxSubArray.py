# find maximum sub arrayw ithin an array 
# psedo code

# maxSum stores the maximum sum 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSum = 0
        len = nums.len()

        for 