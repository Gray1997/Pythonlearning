class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j,n2 in enumerate(reversed(num2)):
                tmp1 = ord(n1) - ord('0')
                tmp2 = ord(n2) - ord('0')
                res[i + j] += tmp1 * tmp2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] ==0:
            res.pop()
        return ''.join(str(v) for v in res)[::-1]