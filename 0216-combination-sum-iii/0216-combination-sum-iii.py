class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def solve (last,total,subset):

           if total > n or len(subset) > k:
              return

           if total == n and len(subset) == k:
               result.append(list(subset))
               return
        
           for i in range(last, 10):
               current_sum = total + i
               subset.append(i)

               solve(i+1, current_sum, subset)

               subset.pop()

        solve(1, 0, [])
        return result