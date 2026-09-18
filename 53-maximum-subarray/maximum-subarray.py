class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        maxsum=nums[0]
        csum=0

        for num in nums:
            csum = max(num,csum+num)
            maxsum =max(maxsum,csum)
        return maxsum