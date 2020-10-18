class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]
        for i in range(len(nums)):
            dp.append(1+max([0]+[dp[j+1]
                                 for j in range(i) if nums[i] > nums[j]]))
        return max(dp)
