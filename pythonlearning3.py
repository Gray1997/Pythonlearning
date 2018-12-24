class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        #print(column_lenth, row_lenth)
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(j)
