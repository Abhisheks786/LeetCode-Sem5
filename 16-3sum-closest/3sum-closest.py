class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest=float('inf')

        for i in range(n):
            l=i+1
            r=n-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]

                
                if abs(curr - target) < abs(closest - target):
                    closest = curr
                if curr>target:
                    r-=1
                else:
                    l+=1
        return closest
        
                

                

        