class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    #    num = x
    #    result = 
    
        num = x
        result = 0

        while num>0:
            id = num % 10
            result =(result * 10) + id
            num = num//10
        return x == result
    # return false