class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        for i in range(0,n-1):
            if arr[i] > arr[i+1]:
                return i