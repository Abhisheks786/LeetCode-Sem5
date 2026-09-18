class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=nums[0]
        csum=0
        cmin=0
        minsum=nums[0]

        for num in nums:
            csum = max(num,csum+num)
            maxsum =max(maxsum,csum)

            cmin = min(num,cmin+num)
            minsum =min(minsum,cmin)
            

        return max(maxsum,abs(minsum))