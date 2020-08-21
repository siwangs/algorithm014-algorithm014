class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, k in enumerate(nums):
            residual = target - k
            if residual in result:
                return sorted([result[residual], i])
            result[k] = i

        return False
