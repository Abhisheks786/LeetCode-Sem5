class Solution:

  def sortedSquares(self, nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)

    
    r = 0
    while r < n and nums[r] < 0:
      r += 1

    l = r - 1

    while l >= 0 and r < n:
      if abs(nums[l]) <= abs(nums[r]):
        ans.append(nums[l] * nums[l])
        l -= 1
      else:
        ans.append(nums[r] * nums[r])
        r += 1

    
    while l >= 0:
      ans.append(nums[l] * nums[l])
      l -= 1
    while r < n:
      ans.append(nums[r] * nums[r])
      r += 1

    return ans