class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        worst = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            temp = best
            best = max(num, num * best, num * worst)
            worst = min(num, num * temp, num * worst)
            ans = max(ans, best)

        return ans