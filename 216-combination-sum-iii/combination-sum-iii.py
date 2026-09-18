from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start: int, curr: list, target: int):
            if len(curr) == k:
                if target == 0:   
                    res.append(list(curr))
                return 
            
            if len(curr)>k or target<0:
                return

            for i in range(start, 10):
                if i > target:
                    break
                
                curr.append(i)
                backtrack(i+1, curr, target - i)
                curr.pop()
        backtrack(1, [], n)
        return res
