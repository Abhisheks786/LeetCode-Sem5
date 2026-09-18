class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []

        def backtrack(start, remain, current):
            if remain == 0:
                results.append(list(current))
                return

            for i in range(start, len(candidates)):
                
                if candidates[i] > remain:
                    break

                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                
                backtrack(i + 1, remain - candidates[i], current)
                current.pop()

        backtrack(0, target, [])
        return results