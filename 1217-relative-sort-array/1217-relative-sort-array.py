class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        frequency = [0] * 1001  
        index = 0  
        for num in arr1:
            frequency[num] += 1
        for num in arr2:
            for _ in range(frequency[num]):
                arr1[index] = num
                index += 1
            frequency[num] = 0
        for num in range(len(frequency)):
            for _ in range(frequency[num]):
                arr1[index] = num
                index += 1
        return arr1
