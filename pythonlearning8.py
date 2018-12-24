class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted(candidates)
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res
    def dfs(self, nums, index, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            else:
                self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], result)
