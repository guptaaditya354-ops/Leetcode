class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def solve(index, total, subset):
            if total == target:
                result.append(list(subset))
                return
            if total > target or index >= len(candidates):
                return
                
            subset.append(candidates[index])
            solve(index, total + candidates[index], subset)

            subset.pop()
            solve(index + 1, total, subset)

        solve(0, 0, [])
        return result
        #     sum = total + nums[index]
        #     subset.pop()
        #     self.solve(index,sum,subset,nums,target,result)
        #     sum = total
        #     subset.pop()
        #     self.solve(index+1,sum,subset,nums,target,result)

        # def combinationSum(self, candidates: list[int], target:int)-> list[list[int]]:
        #     result = []
        #     self.solve (0,0,[],candidates,target,result)
        #     return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        