class Solution:
    def generateMatrix(self, n):

        res = []
        low = n*n + 1
        while low > 1:
            low, high = low - len(res), low
            res = [list(range(low,high))] + list(zip(*A[::-1]))
        return res