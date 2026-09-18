class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
       count=0

       for curr in range(len(nums)):
        if nums[curr]!=0:
            nums[count],nums[curr] =nums[curr],nums[count]
            count+=1


        