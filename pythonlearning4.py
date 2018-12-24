class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_left = self.binaryRearch(nums, target, True)
        if index_left == len(nums) or nums[index_left] != target:
            return [-1,-1]
        index_right = self.binaryRearch(nums,target,False)
        return [index_left, index_right - 1]


    def binaryRearch(self, nums, target, left_flag):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > target or (left_flag and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo
