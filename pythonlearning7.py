class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return [[]]
        res = []
        self.n = len(nums)
        self.dfs(nums, 0, [],res)
        return res

    def dfs(self,nums, target, cur, rst):
        if target == self.n:
            rst.append(cur)
        else:
            for i in nums:
                if i not in cur:
                    self.dfs(nums, target+1, cur + [i],rst)