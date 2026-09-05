class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [c.lower() for c in s if c.isalnum()]
        n = len(filtered)
        left = 0
        right = n - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True
        def func(s,left,right):
            if left>=right:
               return True
            if s[left]!=s[right]:
                return False
            return func(s, left+1, right-1)