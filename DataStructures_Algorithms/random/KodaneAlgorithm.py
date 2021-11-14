class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

sl = Solution()
sl.maxSubArray([2,1,4,-7,3,6,-2,-4,1,3])
