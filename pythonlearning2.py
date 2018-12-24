class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        clen = len(matrix[::-1][0])
        rlen = len(matrix[0])

        
